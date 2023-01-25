from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import DetailView

from app_cart.cart import Cart
from app_product.models import Product
from app_review.forms import ReviewForm
from app_review.models import Review


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
