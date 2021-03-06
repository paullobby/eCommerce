# Generated by Django 3.0.7 on 2020-06-17 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='subtotal',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=100),
        ),
        migrations.AlterField(
            model_name='cart',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
