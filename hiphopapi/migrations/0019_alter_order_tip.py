# Generated by Django 4.2.7 on 2024-01-19 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hiphopapi', '0018_alter_order_tip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='tip',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=7),
        ),
    ]
