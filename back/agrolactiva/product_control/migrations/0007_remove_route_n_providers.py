# Generated by Django 4.1.3 on 2022-11-30 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_control', '0006_alter_providerproductcontrol_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='route',
            name='n_providers',
        ),
    ]
