# Generated by Django 4.2.7 on 2024-01-19 19:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hiphopapi', '0012_rename_closed_order_is_closed_order_date_order_tip_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='hiphopapi.paymenttype'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hiphopapi.ordertype'),
        ),
    ]
