from django.contrib import admin
from .models import *


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'phone_number','address',  'city', 'paid', 'created',
                    'updated','delivery_date','userid']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]


admin.site.register(Order, OrderAdmin)

@admin.register(Ordernow)
class Ordernowadmin(admin.ModelAdmin):
   #list_display=('id','name','amount','status','provider_order_id','payment_id','signature_id',)
   pass

