from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models.signals import post_save


class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

def create_UserProfile(sender, instance, created, **kwargs):
    if created:
        instance.save()
post_save.connect(create_UserProfile, sender=UserProfile)

class Products(models.Model):
    barcode = models.CharField(max_length=255, null=True, blank=True)
    product_description = models.CharField(max_length=255, null=True, blank=True)
    product_name = models.CharField(max_length=255, null=True, blank=True)
    product_brand = models.CharField(max_length=255, null=True, blank=True)
    product_score = models.CharField(max_length=255, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)