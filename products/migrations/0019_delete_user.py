# Generated by Django 4.2.8 on 2024-01-29 05:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_alter_customer_address_alter_customer_age_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
