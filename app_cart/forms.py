from django import forms


class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(widget=forms.NumberInput(
        attrs={'class': 'Amount-input form-input', 'min': '1', 'max': '21', 'size': '2', 'maxlength': '2'}),
        label=''
    )
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
