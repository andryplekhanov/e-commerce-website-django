from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import DetailView
from django_filters.views import FilterView

from app_cart.cart import Cart
from app_product.filters import ProductFilter
from app_product.models import Product, Category
from app_product.utils import get_data_min, get_data_max
from app_review.forms import ReviewForm
from app_review.models import Review
from app_settings.models import SiteSettings


class ProductDetail(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reviews = Review.objects.filter(product=self.get_object()).prefetch_related('user').order_by('-created')
        context['review_form'] = ReviewForm()
        context['reviews'] = reviews

        context['is_product_in_cart'] = False
        cart = Cart(self.request)
        if len(cart) > 0:
            all_ids = cart.get_all_ids()
            if self.kwargs.get('pk') in all_ids:
                context['is_product_in_cart'] = True
        return context

    def post(self, request, pk):
        form = ReviewForm(request.POST)
        if not request.user.is_authenticated:
            raise PermissionDenied()
        if form.is_valid:
            review = form.save(commit=False)
            review.user = request.user
            review.product = self.get_object()
            review.save()
        return HttpResponseRedirect(reverse('product_detail', kwargs={"pk": pk}))


class CategoryView(FilterView):
    paginate_by = 8
    model = Product
    context_object_name = 'products'
    template_name = 'app_product/catalog.html'
    filterset_class = ProductFilter

    def get(self, request, *args, **kwargs):
        self.settings = SiteSettings.load()
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        if not slug:
            self.category = self.settings.root_category
        else:
            self.category = Category.objects.get(slug=slug)
        sub_categories = self.category.get_descendants(include_self=True)
        queryset = Product.objects\
            .select_related('category')\
            .only('name', 'price', 'category')\
            .filter(category__in=sub_categories)\
            .filter(available=True)
        return queryset

    def get_context_data(self, **kwargs):
        _request_copy = self.request.GET.copy()
        parameters = _request_copy.pop('page', True) and _request_copy.urlencode()
        context = super().get_context_data(**kwargs)
        context['title'] = self.category
        qs = self.get_queryset()
        min_price = get_data_min(queryset=qs, root_category=self.settings.root_category)
        max_price = get_data_max(queryset=qs, root_category=self.settings.root_category)
        context['parameters'] = parameters
        context['filter'].form.fields['price'].widget.attrs = {'class': 'range-line',
                                                               'data-type': 'double',
                                                               'data-min': min_price,
                                                               'data-max': max_price}
        return context
