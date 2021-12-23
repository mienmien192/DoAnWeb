from django.db import models

from django.conf import settings
# Create your models here.
class Category(models.Model):
    title = models.CharField(default='', max_length=400)
    slug = models.CharField(default='', max_length=400)
    description = models.TextField(default='')
    active = models.BooleanField(default=True)

def productFile(instance, filename):
    return '/'.join( ['products', str(instance.id), filename] )
class Product(models.Model):
    CATEGORY = (
        ('1', 'Drink'),
        ('2', 'Food'),
        ('3', 'Album'),
        ('4', 'Lightstick'))
    title = models.CharField(default='', max_length=400)
    description = models.TextField(default='')
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    price = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    productImg = models.ImageField(
        upload_to=productFile,
        max_length=254, blank=True, null=True
    )
    def __str__(self):
        return self.title


class Customer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null = True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null = True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total
class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total