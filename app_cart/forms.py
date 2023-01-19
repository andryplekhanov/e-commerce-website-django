from django import forms


class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, max_value=15, label='', widget=forms.NumberInput(attrs={
        'class': 'Amount-input form-input',
        'min': '1', 'max': '15', 'size': '2', 'maxlength': '2',
        'name': "amount", 'type': 'text'
    }))
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
