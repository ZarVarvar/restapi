from .models import Order
from django.forms import ModelForm, TextInput, EmailInput, NumberInput

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['sender', 'senders_address', 'shipped_item', 'FIO', 'email', 'phone_number', 'address_recipient']

        widgets = {
            "sender": TextInput(attrs={
                'class': 'displayblock inputstyle textfamily'
            }),
            "senders_address": TextInput(attrs={
                'class': 'displayblock inputstyle textfamily'
            }),
            "shipped_item": TextInput(attrs={
                'class': 'displayblock inputstyle textfamily'
            }),
            "FIO": TextInput(attrs={
                'class': 'displayblock inputstyle textfamily'
            }),
            "email": EmailInput(attrs={
                'class': 'displayblock inputstyle textfamily'
            }),
            "phone_number": NumberInput(attrs={
                'class': 'displayblock inputstyle textfamily'
            }),
            "address_recipient": TextInput(attrs={
                'class': 'displayblock inputstyle textfamily'
            })
        }

