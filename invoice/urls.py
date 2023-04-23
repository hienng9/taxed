from django.urls import path
from . import views

app_name = "invoice"
urlpatterns = [
    path('dashboard/<int:user_id>', views.dashboard, name="dashboard"),
    path('customer/', views.customer, name="customer"),
    path('products/', views.products, name="products"),
    path('invoices', views.invoices, name='invoices'),
    path('products', views.products, name='products'),
    path('create-invoice/', views.create_invoice, name="create-invoice"),
    path('delete/<slug:slug>', views.delete_invoice, name="delete-invoice"),
    path('create-build-invoice/<slug:slug>', views.create_build_invoice, name="create-build-invoice"),
    path('view-invoice/<slug:slug>',  views.view_invoice, name="view-invoice"),
    path('view-document-invoice/<slug:slug>',  views.view_document_invoice, name="view-document-invoice"),
    
]

