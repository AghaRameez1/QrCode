# Generated by Django 3.0.8 on 2020-07-24 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200724_1238'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='product_brand',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='product_description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='product_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='product_score',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
