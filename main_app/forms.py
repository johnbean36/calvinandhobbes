from django.forms import ModelForm
from .models import Sales

class SalesForm(ModelForm):
    class Meta:
        model = Sales
        fields = ['date', 'price']