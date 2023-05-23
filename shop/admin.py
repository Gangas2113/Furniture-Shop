from django.contrib import admin
from shop.models import *
# Register your models here.

@admin.register(contact)
class contactadmin(admin.ModelAdmin):
    list_display=('fname','lname','email','message')


@admin.register(blog)
class blogadmin(admin.ModelAdmin):
    pass


@admin.register(faq)
class faqadmin(admin.ModelAdmin):
    pass


@admin.register(category)
class categoryadmin(admin.ModelAdmin):
    pass


@admin.register(products)
class productadmin(admin.ModelAdmin):
    pass

@admin.register(gallery)
class galleryadmin(admin.ModelAdmin):
    pass



@admin.register(review)
class reviewadmin(admin.ModelAdmin):
    list_display=('name','email','message')