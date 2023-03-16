from django.forms import ModelForm, widgets
from django.contrib.auth.forms import UserCreationForm
from .models import Room, User, Invoice


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants']

class InvoiceForm(ModelForm):
    class Meta:
        model = Invoice
        fields = '__all__'
        exclude = ['user', 'is_sent']
        widgets = {
            "include_VAT": widgets.Select(attrs={
                'class': 'form-control',
            })}

class CalculatorForm(ModelForm):
    class Meta:
        model = Invoice
        fields = '__all__'
        exclude = ['user', 'name', 'buyer_business_id',
        'is_sent']
        widgets = {
            "include_VAT": widgets.Select(attrs={
                'class': 'form-control',
            })}

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'name', 'username', 'email', 'bio']
