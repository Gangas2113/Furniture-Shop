from django.db import models
from shop.models import products

from django.db.models.fields import CharField
from django.utils.translation import gettext_lazy as _
from .constants import PaymentStatus
from django.contrib.auth.models import User

class Ordernow(models.Model):
    name = CharField(_("Customer Name"), max_length=254, blank=False, null=False)
    amount = models.FloatField(_("Amount"), null=False, blank=False)
    status = CharField(
        _("Payment Status"),
        default=PaymentStatus.PENDING,
        max_length=254,
        blank=False,
        null=False,
    )
    provider_order_id = models.CharField(
        _("Order ID"), max_length=40, null=False, blank=False
    )
    payment_id = models.CharField(
        _("Payment ID"), max_length=36, null=False, blank=False
    )
    signature_id = models.CharField(
        _("Signature ID"), max_length=128, null=False, blank=False
    )

    def __str__(self):
        return f"{self.id}-{self.name}-{self.status}"

MYCITY=(
    ('Amritsar','Amritsar'),
    ('Bathinda','Bathinda'),
    ('Barnala','Barnala'),
    ('Bajakhana','Bajakhana'),
    ('Bhucho Mandi','Bhucho Mandi'),
    ('Dabawali','Dabawali'),
    ('Faridkot','Faridkot'),
    ('Goniana','Goniana'),
    ('Jaito','Jaito'),
    ('Jalandhar','Jalandhar'),
    ('Khanna','Khanna'),
    ('Kaliawali','Kaliawali'),
    ('Kotakpura','Kotakpura'),
    ('Ludhiana','Ludhiana'),
    ('Malout','Malout'),
    ('Maur Mandi','Maur Mandi'),
    ('Malerkotla','Malerkotla'),
    ('Moga','Moga'),
    ('Muktsar','Muktsar'),
    ('Patiala','Patiala'),
    ('Rajpura','Rajpura'),
    ('Rampura','Rampura'),
    ('Sunam','Sunam'),
    ('Sangrur','Sangrur'),
    ('Talwandi Sabo','Talwandi Sabo'),
)
class Order(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField()
    phone_number=models.CharField(max_length=10,default="")
    address = models.CharField(max_length=150)
    
    city = models.CharField(max_length=100,choices=MYCITY)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    delivery_date=models.CharField(max_length=10,default="")
    userid=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)

    class Meta:
        ordering = ('-created', )

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())



class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(products, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity

