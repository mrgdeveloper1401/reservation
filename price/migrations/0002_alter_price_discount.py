# Generated by Django 5.0 on 2023-12-20 17:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coupon_management', '0002_alter_allowedusersrule_options_and_more'),
        ('price', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='discount',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='coupon_management.couponuser'),
        ),
    ]