# Generated by Django 3.0.4 on 2020-03-19 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0003_auto_20200319_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockdata',
            name='date',
            field=models.DateTimeField(),
        ),
    ]