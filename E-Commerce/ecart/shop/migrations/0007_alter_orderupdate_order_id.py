# Generated by Django 4.2.4 on 2024-02-17 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_orderupdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderupdate',
            name='order_id',
            field=models.IntegerField(default='', max_length=50),
        ),
    ]