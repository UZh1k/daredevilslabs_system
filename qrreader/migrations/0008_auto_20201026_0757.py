# Generated by Django 3.1.1 on 2020-10-26 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qrreader', '0007_auto_20201023_1409'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='course',
        ),
        migrations.AddField(
            model_name='client',
            name='courses',
            field=models.ManyToManyField(blank=True, to='qrreader.Course'),
        ),
    ]
