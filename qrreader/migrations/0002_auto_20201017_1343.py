# Generated by Django 3.1.1 on 2020-10-17 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qrreader', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='clients_came',
            field=models.ManyToManyField(blank=True, to='qrreader.Client'),
        ),
    ]
