# Generated by Django 4.1.3 on 2024-01-19 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hiphopapi', '0016_alter_order_payment_alter_order_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=7),
        ),
    ]
