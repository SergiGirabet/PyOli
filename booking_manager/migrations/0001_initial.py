# Generated by Django 3.1.7 on 2021-05-23 08:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_field', models.CharField(max_length=150)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'addresses',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_order', models.DateTimeField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('expected_delivery_date', models.DateTimeField()),
                ('status', models.CharField(choices=[('PENDING', 'Pending'), ('PREPARING', 'Preparing'), ('DELIVERING', 'Delivering'), ('COMPLETED', 'Completed')], default='PENDING', max_length=15)),
                ('deliver_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking_manager.address')),
                ('order_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('stock', models.IntegerField()),
                ('modifiable', models.BooleanField()),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking_manager.category')),
            ],
            options={
                'ordering': ['product_category'],
            },
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capacity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ProductOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking_manager.order')),
                ('ordered_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking_manager.product')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time_zone', models.CharField(choices=[('1', '12:30 - 14:00'), ('2', '14:00 - 15:30'), ('3', '21:00 - 22:30'), ('4', '22:30 - 00:00')], max_length=14, null=True)),
                ('people_number', models.IntegerField()),
                ('booking_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('reserved_table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking_manager.table')),
            ],
        ),
    ]
