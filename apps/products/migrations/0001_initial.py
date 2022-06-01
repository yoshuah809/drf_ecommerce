# Generated by Django 4.0.4 on 2022-06-01 19:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MeasureUnit',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('date_created', models.DateField(auto_now_add=True, verbose_name='Date Created')),
                ('date_modified', models.DateField(auto_now=True, verbose_name='Date Modified')),
                ('date_deleted', models.DateField(auto_now=True, verbose_name='Date Deleted')),
                ('description', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name': 'MeasureUnit',
                'verbose_name_plural': 'MeasureUnits',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('date_created', models.DateField(auto_now_add=True, verbose_name='Date Created')),
                ('date_modified', models.DateField(auto_now=True, verbose_name='Date Modified')),
                ('date_deleted', models.DateField(auto_now=True, verbose_name='Date Deleted')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Product Name')),
                ('description', models.TextField(unique=True, verbose_name='Product Description')),
                ('image', models.ImageField(upload_to='products/', verbose_name='Product Image')),
            ],
            options={
                'verbose_name': 'On Sale Indicator',
                'verbose_name_plural': 'On Sale Indicators',
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('date_created', models.DateField(auto_now_add=True, verbose_name='Date Created')),
                ('date_modified', models.DateField(auto_now=True, verbose_name='Date Modified')),
                ('date_deleted', models.DateField(auto_now=True, verbose_name='Date Deleted')),
                ('description', models.CharField(max_length=50, unique=True, verbose_name='Description')),
                ('measure_unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.measureunit', verbose_name='Measure Unit')),
            ],
            options={
                'verbose_name': 'ProductCategory',
                'verbose_name_plural': 'ProductCategories',
            },
        ),
        migrations.CreateModel(
            name='OnSaleInicator',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('date_created', models.DateField(auto_now_add=True, verbose_name='Date Created')),
                ('date_modified', models.DateField(auto_now=True, verbose_name='Date Modified')),
                ('date_deleted', models.DateField(auto_now=True, verbose_name='Date Deleted')),
                ('discount_value', models.SmallIntegerField(default=0)),
                ('category_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.productcategory', verbose_name='On Sale Inicator')),
            ],
            options={
                'verbose_name': 'On Sale Indicator',
                'verbose_name_plural': 'On Sale Indicators',
            },
        ),
        migrations.CreateModel(
            name='HistoricalProductCategory',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('date_created', models.DateField(blank=True, editable=False, verbose_name='Date Created')),
                ('date_modified', models.DateField(blank=True, editable=False, verbose_name='Date Modified')),
                ('date_deleted', models.DateField(blank=True, editable=False, verbose_name='Date Deleted')),
                ('description', models.CharField(db_index=True, max_length=50, verbose_name='Description')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('measure_unit', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='products.measureunit', verbose_name='Measure Unit')),
            ],
            options={
                'verbose_name': 'historical ProductCategory',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalProduct',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('date_created', models.DateField(blank=True, editable=False, verbose_name='Date Created')),
                ('date_modified', models.DateField(blank=True, editable=False, verbose_name='Date Modified')),
                ('date_deleted', models.DateField(blank=True, editable=False, verbose_name='Date Deleted')),
                ('name', models.CharField(db_index=True, max_length=150, verbose_name='Product Name')),
                ('description', models.TextField(db_index=True, verbose_name='Product Description')),
                ('image', models.TextField(max_length=100, verbose_name='Product Image')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical On Sale Indicator',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalOnSaleInicator',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('date_created', models.DateField(blank=True, editable=False, verbose_name='Date Created')),
                ('date_modified', models.DateField(blank=True, editable=False, verbose_name='Date Modified')),
                ('date_deleted', models.DateField(blank=True, editable=False, verbose_name='Date Deleted')),
                ('discount_value', models.SmallIntegerField(default=0)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('category_product', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='products.productcategory', verbose_name='On Sale Inicator')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical On Sale Indicator',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalMeasureUnit',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('date_created', models.DateField(blank=True, editable=False, verbose_name='Date Created')),
                ('date_modified', models.DateField(blank=True, editable=False, verbose_name='Date Modified')),
                ('date_deleted', models.DateField(blank=True, editable=False, verbose_name='Date Deleted')),
                ('description', models.CharField(db_index=True, max_length=50)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical MeasureUnit',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]