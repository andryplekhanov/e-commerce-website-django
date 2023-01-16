from django import forms
from .models import *


# class OrderCreateForm(forms.ModelForm):
#     class Meta:
#         model = Order
#         fields = '__all__'
#         widgets = {
#             'user': forms.HiddenInput(),
#             'paid': forms.HiddenInput(),
#             'total_cost': forms.HiddenInput()
#         }
