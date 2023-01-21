from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.db.models import Count
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import DetailView

# from app_cart.forms import CartAddProductForm
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
        # context['cart_form'] = CartAddProductForm(initial={'quantity': 1})
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
