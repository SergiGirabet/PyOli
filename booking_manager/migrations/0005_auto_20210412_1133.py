# Generated by Django 3.1.7 on 2021-04-12 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_manager', '0004_product_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(),
        ),
    ]