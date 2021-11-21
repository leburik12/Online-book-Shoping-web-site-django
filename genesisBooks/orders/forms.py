from django import forms
from .models import Order
from django.utils.translation import gettext_lazy as _

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city', 'phone_number_1','phone_number_2']

        help_texts = {
        'phone_number_2': _('In case if phone number 1 does\'t work(Optional)'),
        }
