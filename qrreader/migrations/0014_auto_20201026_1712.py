# Generated by Django 3.1.1 on 2020-10-26 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qrreader', '0013_auto_20201026_1658'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lesson',
            options={'ordering': ['date']},
        ),
    ]
