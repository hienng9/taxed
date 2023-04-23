from django.db import models
from base.models import User
from uuid import uuid4
from django.utils import timezone 
from django.template.defaultfilters import slugify

class Customer(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    business_id = models.CharField(blank = True, max_length=100, null=True)
    postal_code = models.CharField(max_length=10, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    telephone = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(unique=True, null=True)

    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    uniqueId = models.CharField(blank = True, max_length=100, null=True)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    updated = models.DateTimeField()
    created = models.DateTimeField()


    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return f"{self.name} - {self.business_id}"

    def save(self, *args, **kwargs):
        if self.created is None:
            self.created = timezone.localtime(timezone.now())

        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify(f"{self.name} - {self.business_id}")

        self.slug = slugify(f"{self.name} - {self.business_id}")
        self.updated = timezone.localtime(timezone.now())
        super(Customer, self).save(*args, **kwargs)

class Invoice(models.Model):
    TERMS = [
        ('14 days', '14 days'),
        ('30 days', '30 days'), 
        ('60 days', '60 days')
    ]

    STATUS = [
        ('INCOMPLETE', 'INCOMPLETE'),
        ('SENT', 'SENT'),
        ('OVERDUE', 'OVERDUE'),
        ('PAID', 'PAID'), 
        
    ]

    name = models.CharField(null=True, blank=True, max_length=100)
    number = models.CharField(null=True, blank=True, max_length=100)
    due_date = models.DateField(null=True, blank=True)
    payment_terms = models.CharField(choices=TERMS, default='14 days', max_length=100)
    status = models.CharField(choices=STATUS, default='CURRENT', max_length=100)
    notes = models.TextField(null=True, blank=True)

    customer = models.ForeignKey(Customer, blank=True, null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    updated = models.DateTimeField()
    created = models.DateTimeField()

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return f"{self.number} - {self.uniqueId}"

    def save(self, *args, **kwargs):
        if self.created is None:
            self.created = timezone.localtime(timezone.now())

        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify(f"{self.number} - {self.uniqueId}")

        self.slug = slugify(f"{self.number} - {self.uniqueId}")
        self.updated = timezone.localtime(timezone.now())
        super(Invoice, self).save(*args, **kwargs)

class Product(models.Model):
    
    CURRENCY = [
        ('$', 'USD'),
        ('€', 'EUR')
    ]
    name = models.CharField(null=True, blank=True, max_length=100)
    description = models.TextField(null=True, blank=True)
    quantity = models.FloatField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    vat_rate = models.FloatField(null=True, blank=True)
    price_wo_VAT = models.FloatField(null=True, blank=True)
    currency = models.CharField(choices=CURRENCY, default='€', max_length=100)

    invoice = models.ForeignKey(Invoice, null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    updated = models.DateTimeField()
    created = models.DateTimeField()

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return f"{self.name} - {self.uniqueId}"

    def save(self, *args, **kwargs):
        if self.created is None:
            self.created = timezone.localtime(timezone.now())

        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify(f"{self.name} - {self.uniqueId}")

        self.slug = slugify(f"{self.name} - {self.uniqueId}")
        self.updated = timezone.localtime(timezone.now())
        super(Product, self).save(*args, **kwargs)

class Settings(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    business_id = models.CharField(blank = True, max_length=100, null=True)
    postal_code = models.CharField(max_length=10, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    telephone = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(unique=True, null=True)

    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    uniqueId = models.CharField(blank = True, max_length=100, null=True)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    updated = models.DateTimeField()
    created = models.DateTimeField()


    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return f"{self.name} - {self.business_id}"
    
    # def get_absolute_url(self):
    #     return reverse('settings-detail', kwargs = {'slug':self.slug})

    def save(self, *args, **kwargs):
        if self.created is None:
            self.created = timezone.localtime(timezone.now())

        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify(f"{self.name} - {self.business_id}")

        self.slug = slugify(f"{self.name} - {self.business_id}")
        self.updated = timezone.localtime(timezone.now())
        super(Customer, self).save(*args, **kwargs)