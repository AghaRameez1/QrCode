from django.contrib import admin

# Register your models here.
from api.models import UserProfile, Products


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user','name','created_at','modified_at']
admin.site.register(UserProfile,UserProfileAdmin)



class ProductsAdmin(admin.ModelAdmin):
    list_display = ['barcode','product_description','product_name','product_brand','product_score','created_at','modified_at']
admin.site.register(Products,ProductsAdmin)