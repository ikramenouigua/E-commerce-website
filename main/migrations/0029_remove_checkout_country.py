# Generated by Django 3.1.8 on 2021-05-23 23:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0028_auto_20210523_1713'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkout',
            name='country',
        ),
    ]