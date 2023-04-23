from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from base.models import User
from django.db.models import Q
from .models import *
from uuid import uuid4

from .forms import CustomerForm, ProductForm, InvoiceForm, CustomerSelectForm
# Create your views here.

@login_required
def dashboard(request, user_id):
    user = User.objects.get(id = user_id)
    if request.user != user:
        return Http404
    context = {}
    return render(request, 'invoice/dashboard.html', context)

@login_required
def customer(request):
    user = User.objects.get(id = request.user.id)
    customers = user.customer_set.all()

    if request.method != "POST":
        form = CustomerForm()
    
    else:
        form = CustomerForm(request.POST)

        if form.is_valid():
            cust = form.save(commit=False)
            cust.user = user
            cust.save()
            messages.success(request, "New Customer Added")
            return redirect('invoice:customer')
        else:
            messages.error(request, "Problem occured. Please try again")
            return redirect('invoice:customer')
        

    context = {'customers': customers, 'form': form}
    return render(request, 'invoice/customer.html', context)

@login_required
def products(request):
    user = User.objects.get(id = request.user.id)
    products = user.product_set.all()

    context = {"products": products}
    return render(request, 'invoice/products.html', context)

@login_required
def invoices(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    user = User.objects.get(id = request.user.id)
    invoices_set = user.invoice_set.all()
    invoices = invoices_set.filter(
        Q(number__icontains=q)|
        Q(name__icontains=q)|
        Q(customer__name__icontains=q)
    )
    context = {"invoices": invoices}
    return render(request, 'invoice/invoices.html', context)
    
@login_required
def create_invoice(request):
    user = User.objects.get(id = request.user.id)
    number = 'INV-' + str(uuid4()).split('-')[4]
    new_invoice = Invoice.objects.create(number = number)
    new_invoice.user = user
    new_invoice.save()

    inv = Invoice.objects.get(number = number)
    return redirect('invoice:create-build-invoice', slug = inv.slug)

@login_required
def create_build_invoice(request, slug):
    #fetch the invoice
    try:
        invoice = Invoice.objects.get(slug = slug)
    except:
        messages.error(request, "Something went wrong")
        return redirect('invoice:invoices')

    # fetch products
    products = invoice.product_set.all()

    context = {'products': products, 'invoice': invoice}

    if request.method == "GET":
        prod_form = ProductForm()
        inv_form = InvoiceForm(instance = invoice)  
        customer_form = CustomerSelectForm(initial_customer = invoice.customer, user = invoice.user, instance = invoice )  
        context['prod_form'] = prod_form
        context['inv_form'] = inv_form
        context['customer_form'] = customer_form
        print(context)
        return render(request, 'invoice/create-invoice.html', context)

    if request.method == "POST":
        prod_form = ProductForm(request.POST)
        inv_form = InvoiceForm(request.POST, instance = invoice)   
        print("user", invoice.user)
        customer_form = CustomerSelectForm(request.POST, initial_customer = invoice.customer, user = invoice.user, instance = invoice )
        if prod_form.is_valid():
            prod = prod_form.save(commit = False)
            prod.user = invoice.user
            prod.invoice = invoice
            if prod.vat_rate == 0:
                prod.price_wo_VAT = prod.price
            else:
                prod.price_wo_VAT = round(prod.price / (1+(prod.vat_rate/100)),2)
            prod.save()
            messages.success(request, "Product added successfully")
            return redirect('invoice:create-build-invoice', slug = invoice.slug)
        elif inv_form.is_valid() and 'payment_terms' in request.POST:
            inv_form.save()
            messages.success(request, "Invoice updated succesfully")
            return redirect('invoice:create-build-invoice', slug=slug)
        elif customer_form.is_valid() and 'customer' in request.POST:
            customer_form.save()
            messages.success(request, "Client added to invoice succesfully")
            return redirect('invoice:create-build-invoice', slug=slug)
        else:
            context['prod_form'] = prod_form
            context['inv_form'] = inv_form
            messages.error(request, "Error happened. Please try again")
            return render(request, 'invoice/create-invoice.html', context)
            
    return render(request, 'invoice/create-invoice.html', context)

@login_required
def view_invoice(request, slug):
    try:
        invoice = Invoice.objects.get(slug=slug)
        pass
    except:
        messages.error(request, 'Something went wrong')
        return redirect('invoices')

    #fetch all the products - related to this invoice
    products = Product.objects.filter(invoice=invoice)

    #Get Client Settings
    p_settings = User.objects.get(id = request.user.id)

    #Calculate the Invoice Total
    invoiceCurrency = ''
    invoiceTotal = 0.0
    invoiceTotalWithOutVAT = 0.0
    if len(products) > 0:
        for product in products:
            invoiceTotalWithOutVAT += product.price_wo_VAT
            invoiceTotal += product.price
            invoiceCurrency = product.currency



    context = {}
    context['invoice'] = invoice
    context['products'] = products
    context['p_settings'] = p_settings
    context['invoiceTotal'] = "{:.2f}".format(invoiceTotal)
    context['invoiceTotalWithOutVAT'] = "{:.2f}".format(invoiceTotalWithOutVAT)
    context['invoiceCurrency'] = invoiceCurrency
    return render(request, 'invoice/view-invoice.html', context)

@login_required
def view_document_invoice(request, slug):
    return render(request, 'invoice/view-document-invoice.html')

def delete_invoice(request, slug):
    try:
        Invoice.objects.get(slug=slug).delete()
    except:
        messages.error(request, 'Something went wrong')
        return redirect('invoice:invoices')

    return redirect('invoice:invoices')
# http://127.0.0.1:8000/invoice/create-build-invoice/inv-3926f1eb95cd-2a90f1b298cf
