# Generated by Django 4.1.3 on 2022-11-22 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product_control', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productdispatch',
            options={'ordering': ['id_route', 'id_dispatched_by', 'id_client', 'dispatch_date', 'quantity'], 'verbose_name_plural': 'Product Dispatch'},
        ),
        migrations.AlterModelOptions(
            name='providerproductcontrol',
            options={'ordering': ['id_provider', 'id_delivery', 'quantity', 'id_provider_price', 'payment_amount'], 'verbose_name_plural': 'Provider Product Control'},
        ),
        migrations.RenameField(
            model_name='client',
            old_name='person',
            new_name='id_person',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='municipality',
            new_name='id_municipality',
        ),
        migrations.RenameField(
            model_name='productdispatch',
            old_name='dispatch_product_quantity',
            new_name='quantity',
        ),
        migrations.RenameField(
            model_name='provider',
            old_name='route',
            new_name='id_route',
        ),
        migrations.RenameField(
            model_name='providerproductcontrol',
            old_name='provider_price',
            new_name='id_provider_price',
        ),
        migrations.RenameField(
            model_name='providerproductcontrol',
            old_name='total_price',
            new_name='payment_amount',
        ),
        migrations.RemoveField(
            model_name='providerproductcontrol',
            name='delivery_date',
        ),
        migrations.AddField(
            model_name='productdispatch',
            name='id_delivery',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='product_control.delivery'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='billinginfo',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='contactinfo',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]