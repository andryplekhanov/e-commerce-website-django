from django.db.models import Min
from django.views.generic import TemplateView
from app_product.models import Category, Product
from django.db.models import Sum

from app_settings.models import SiteSettings


class IndexView(TemplateView):
    template_name = 'app_main/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        context['limited'] = Product.objects\
            .filter(available=True, limited=True)\
            .select_related('category')\
            .only('category', 'name', 'price')

        settings = SiteSettings.load()
        context['populars'] = Product.objects\
            .prefetch_related('order_items')\
            .filter(available=True)\
            .only('category', 'name', 'price')\
            .annotate(total=Sum('order_items__quantity'))\
            .order_by('-total')[:settings.quantity_popular]

        return context
