# Generated by Django 4.2.7 on 2024-01-19 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hiphopapi', '0017_alter_order_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='tip',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=7),
        ),
    ]