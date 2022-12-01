# Generated by Django 4.1.3 on 2022-12-01 18:15

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('product_control', '0010_remove_employee_id_route'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='providerpayment',
            name='id_billing_info',
        ),
        migrations.AddField(
            model_name='providerpayment',
            name='total_amount',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='providerproductcontrol',
            name='payment_amount',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='route',
            name='n_providers',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='providerpayment',
            name='payment_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='providerpayment',
            name='payment_since',
            field=models.DateField(default=datetime.datetime(2022, 11, 16, 18, 14, 55, 15955, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='providerpayment',
            name='payment_until',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
