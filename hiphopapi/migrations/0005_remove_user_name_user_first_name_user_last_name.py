# Generated by Django 4.2.7 on 2024-01-13 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hiphopapi', '0004_ordertype_paymenttype'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(default='', max_length=50),
        ),
    ]
