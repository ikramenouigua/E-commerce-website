# Generated by Django 3.2 on 2021-05-18 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_alter_product_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
