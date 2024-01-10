# Generated by Django 4.1.3 on 2024-01-10 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hiphopapi', '0003_orderitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=50)),
            ],
        ),
    ]