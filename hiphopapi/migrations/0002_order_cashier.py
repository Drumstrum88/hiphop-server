# Generated by Django 4.1.3 on 2024-01-09 02:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hiphopapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='cashier',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='hiphopapi.user'),
        ),
    ]