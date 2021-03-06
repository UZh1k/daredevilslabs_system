# Generated by Django 3.1.1 on 2020-10-23 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qrreader', '0005_remove_lesson_qr_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='clients_came',
            field=models.ManyToManyField(blank=True, null=True, to='qrreader.Client'),
        ),
    ]
