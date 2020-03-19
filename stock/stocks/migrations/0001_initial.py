# Generated by Django 3.0.4 on 2020-03-19 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=2048)),
                ('symbol', models.CharField(max_length=2048)),
                ('sector', models.CharField(max_length=2048)),
            ],
        ),
        migrations.CreateModel(
            name='StockData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('open_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('close_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('high_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('low_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('volume', models.IntegerField(default=0)),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='data', to='stocks.Stock')),
            ],
        ),
    ]