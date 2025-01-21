# Generated by Django 5.1.4 on 2025-01-18 06:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Court',
            fields=[
                ('id_court', models.AutoField(primary_key=True, serialize=False)),
                ('name_court', models.CharField(max_length=255)),
                ('cost_court', models.DecimalField(decimal_places=2, max_digits=10)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('type_court', models.CharField(choices=[('Indoor', 'Indoor'), ('Outdoor', 'Outdoor')], max_length=255)),
                ('status', models.CharField(choices=[('Closed', 'Closed'), ('Maintenance', 'Maintenance'), ('Available', 'Available')], max_length=50)),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('name', models.CharField(max_length=255)),
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('phone', models.CharField(max_length=10, unique=True)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('booking_id', models.AutoField(primary_key=True, serialize=False)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('booking_date', models.DateField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='home.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('payment_id', models.AutoField(primary_key=True, serialize=False)),
                ('payment_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed'), ('Failed', 'Failed')], max_length=50)),
                ('method', models.CharField(choices=[('Credit Card', 'Credit Card'), ('Debit Card', 'Debit Card'), ('Cash', 'Cash'), ('Online', 'Online')], max_length=50)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='home.booking')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='home.customer')),
            ],
        ),
    ]
