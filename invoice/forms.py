from django import forms
from django.contrib.auth.models import User
from django.forms import widgets
from .models import *
import json

#Form Layout from Crispy Forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

class DateInput(forms.DateInput):
    input_type = 'date'

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'address', 'business_id', 
                  'postal_code', 'city', 'telephone', 'email']

        
class InvoiceForm(forms.ModelForm):
    THE_OPTIONS = [
    ('14 days', '14 days'),
    ('30 days', '30 days'),
    ('60 days', '60 days'),
    ]
    STATUS_OPTIONS = [
    ('INCOMPLETE', 'INCOMPLETE'),
    ('OVERDUE', 'OVERDUE'),
    ('PAID', 'PAID'),
    ]

    name = forms.CharField(
                    required = True,
                    label='Invoice Name or Title',
                    widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Enter Invoice Name'}),)
    payment_terms = forms.ChoiceField(
                    choices = THE_OPTIONS,
                    required = True,
                    label='Select Payment Terms',
                    widget=forms.Select(attrs={'class': 'form-control mb-3'}),)
    status = forms.ChoiceField(
                    choices = STATUS_OPTIONS,
                    required = True,
                    label='Invoice Status',
                    widget=forms.Select(attrs={'class': 'form-control mb-3'}),)
    notes = forms.CharField(
                    required = True,
                    label='Enter any notes for the client',
                    widget=forms.Textarea(attrs={'class': 'form-control mb-3'}))

    due_date = forms.DateField(
                        required = True,
                        label='Invoice Due',
                        widget=DateInput(attrs={'class': 'form-control mb-3'}),)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group col-md-6'),
                Column('number', css_class='form-group col-md-6'),
                css_class='form-row'),
            
            Row(
                Column('payment_terms', css_class='form-group col-md-6'),
                Column('due_date', css_class='form-group col-md-6'),
                css_class='form-row'),
            Row(
                Column('status', css_class='form-group col-md-6'),
                Column('notes', css_class='form-group col-md-6'),
                css_class='form-row'),

            Submit('submit', ' SAVE '))

    class Meta:
        model = Invoice
        fields = ['name', 'number', 'due_date', 
                  'payment_terms', 'status', 
                  'notes']
        
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'quantity', 
                  'price', 'vat_rate', 'currency']

class SettingsForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'address', 'business_id', 
                  'postal_code', 'city', 'phone', 'email']
        
class CustomerSelectForm(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        self.initial_client = kwargs.pop('initial_customer')
        self.user = kwargs.pop('user')
        self.CUSTOMER_LIST = Customer.objects.filter(user = self.user)
        self.CUSTOMER_CHOICES = [('-----', '--Select a Customer--')]


        for customer in self.CUSTOMER_LIST:
            d_t = (customer.uniqueId, customer.name)
            self.CUSTOMER_CHOICES.append(d_t)


        super(CustomerSelectForm,self).__init__(*args,**kwargs)

        self.fields['customer'] = forms.ChoiceField(
                                        label='Choose a customer',
                                        choices = self.CUSTOMER_CHOICES,
                                        widget=forms.Select(attrs={'class': 'form-control mb-3'}),)

    class Meta:
        model = Invoice
        fields = ['customer']


    def clean_customer(self):
        c_customer = self.cleaned_data['customer']
        print(c_customer)
        if c_customer == '-----':
            return self.initial_client
        else:
            return Customer.objects.get(uniqueId=c_customer)
        

    