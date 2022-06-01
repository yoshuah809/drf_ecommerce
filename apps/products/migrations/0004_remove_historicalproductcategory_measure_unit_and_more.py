# Generated by Django 4.0.4 on 2022-06-01 21:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_historicalproduct_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalproductcategory',
            name='measure_unit',
        ),
        migrations.RemoveField(
            model_name='productcategory',
            name='measure_unit',
        ),
        migrations.AddField(
            model_name='historicalproduct',
            name='category_product',
            field=models.ForeignKey(blank=True, db_constraint=False, default=1, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='products.productcategory', verbose_name='Product Category'),
        ),
        migrations.AddField(
            model_name='historicalproduct',
            name='measure_unit',
            field=models.ForeignKey(blank=True, db_constraint=False, default=1, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='products.measureunit', verbose_name='Measure Unit'),
        ),
        migrations.AddField(
            model_name='product',
            name='category_product',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.productcategory', verbose_name='Product Category'),
        ),
        migrations.AddField(
            model_name='product',
            name='measure_unit',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='products.measureunit', verbose_name='Measure Unit'),
        ),
    ]