from django import forms
from app_orders.models import Order
from django.utils.translation import gettext_lazy as _


class OrderCreateForm(forms.ModelForm):
    address = forms.CharField(max_length=255, label=_("Адрес доставки"), required=True,
                              widget=forms.TextInput(attrs={
                                  'class': 'form-input',
                                  'maxlength': '255',
                                  'data-validate': 'require',
                                  'autocomplete': 'address'
                              }))
    city = forms.CharField(max_length=100, label=_("Город доставки"), required=True,
                           widget=forms.TextInput(attrs={
                               'class': 'form-input',
                               'maxlength': '100',
                               'data-validate': 'require',
                               'autocomplete': 'city'
                           }))
    card_number = forms.CharField(min_length=8, max_length=9, required=True, label=_('Номер карты'),
                                  widget=forms.TextInput(attrs={
                                      'class': 'form-input',
                                      'data-validate': 'requireCard'
                                  }))

    class Meta:
        model = Order
        fields = ['address', 'city', 'delivery_type', 'payment_type', 'card_number']
        widgets = {
            'delivery_type': forms.RadioSelect,
            'payment_type': forms.RadioSelect
        }


class OrderPaymentForm(forms.ModelForm):
    card_number = forms.CharField(min_length=8, max_length=9, required=True, label=_('Номер карты'),
                                  widget=forms.TextInput(attrs={
                                      'class': 'form-input',
                                      'data-validate': 'requireCard'
                                  }))

    class Meta:
        model = Order
        fields = ['payment_type', 'card_number']
        widgets = {'payment_type': forms.RadioSelect}
