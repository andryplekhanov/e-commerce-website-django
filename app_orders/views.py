from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import FormMixin

from app_cart.cart import Cart
from app_orders.forms import OrderCreateForm
from app_orders.models import Order, OrderItem
from app_orders.utils import get_delivery_price
from app_settings.models import SiteSettings
from app_users.forms import CreationUserForm
from app_users.views import AUTH_MENU


class OrdersHistory(LoginRequiredMixin, ListView):
    raise_exception = True
    model = Order
    extra_context = {'menu': AUTH_MENU,
                     'breadcrumbs': [_('Личный кабинет'), _('История заказов')],
                     'title': _('История заказов'),
                     'current_elem': 'orders_history'
                     }

    def get_queryset(self):
        queryset = Order.objects.filter(user=self.request.user)\
            .only('id', 'created', 'paid', 'delivery_type', 'payment_type', 'paid', 'status')
        return queryset


class OrderDetail(LoginRequiredMixin, DetailView):
    raise_exception = True
    model = Order

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.user != self.request.user:
            raise PermissionDenied
        return obj


class OrderView(FormMixin, TemplateView):
    template_name = 'app_orders/create_order.html'
    form_class = OrderCreateForm
    raise_exception = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = Cart(self.request)
        total_cost = cart.get_total_price()
        choices = []
        settings = SiteSettings.load()
        common_delivery_price = settings.common_delivery_price
        edge_for_free_delivery = settings.edge_for_free_delivery
        express_delivery_price = settings.express_delivery_price

        context['common_delivery_price'] = 0
        context['total_cost'] = total_cost

        if total_cost < edge_for_free_delivery:
            choices.append(('1', f'Обычная доставка (+{common_delivery_price} ₽)'))
            context['common_delivery_price'] = common_delivery_price
        else:
            choices.append(('1', f'Обычная доставка (бесплатно)'))

        choices.append(('2', f'Экспресс доставка (+{express_delivery_price} ₽)'))
        context['form'].fields['delivery_type'].widget.choices = choices

        if self.request.user.is_authenticated:
            instance = self.request.user
            context['form_reg'] = CreationUserForm(instance=instance)
            context['form_reg'].fields['email'].disabled = True
            context['form_reg'].fields['full_name'].disabled = True
            context['form_reg'].fields['phone_number'].disabled = True
        else:
            context['form_reg'] = CreationUserForm()
        return context

    def post(self, request):
        cart = Cart(request)
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.data = form.cleaned_data
            order.user = request.user
            order.delivery_price = get_delivery_price(total=cart.get_total_price(),
                                                      type_delivery=form.cleaned_data['delivery_type'])
            order = form.save()
            items_to_insert = [
                OrderItem(order=order, product=item['product'], price=item['price'], quantity=item['quantity'])
                for item in cart
            ]
            OrderItem.objects.bulk_create(items_to_insert)

            cart.clear()
            # messages.success(request, 'Заказ успешно добавлен.')
            # messages.info(request, 'Ждём подтверждения оплаты от платёжной системы.')
            # order_created.delay(order.id)
            return HttpResponseRedirect(reverse('order_detail', args=[order.id]))
        return super().form_invalid(form)
