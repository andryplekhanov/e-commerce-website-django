from django import forms
from django.forms import ModelForm
from app_review.models import Review
from django.utils.translation import gettext_lazy as _


class ReviewForm(ModelForm):
    text = forms.CharField(max_length=1000, required=True,
                           widget=forms.Textarea(attrs={
                               'class': 'form-textarea',
                               'data-validate': 'require',
                               'placeholder': _('Напишите свой отзыв')
                           }))

    class Meta:
        model = Review
        fields = ('text',)
