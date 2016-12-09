from django import forms
from .models import Pedido
from django.contrib.auth.forms import UserCreationForm


class OrderForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ('__all__')

class User_Form(UserCreationForm):
    puesto = forms.CharField(max_length = 64)
