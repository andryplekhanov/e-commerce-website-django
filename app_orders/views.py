from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from app_users.views import AUTH_MENU
from app_orders.models import Order
from django.utils.translation import gettext_lazy as _


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
        object = super().get_object(queryset)
        if object.user != self.request.user:
            raise PermissionDenied
        return object
