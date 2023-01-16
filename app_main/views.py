from django.db.models import Min
from django.views.generic import TemplateView
from app_product.models import Category, Product


class IndexView(TemplateView):
    template_name = 'app_main/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        # TODO категории задаются в настройках
        categories = Category.objects.filter(parent__isnull=False)[:3]
        cats = {}
        for cat in categories:
            cats[cat] = Product.objects.filter(category=cat).filter(available=True).only('price').aggregate(Min('price'))
        context['cats'] = cats

        limited = Product.objects.filter(available=True, limited=True).select_related('category').only('category', 'name', 'price')
        context['limited'] = limited

        return context
