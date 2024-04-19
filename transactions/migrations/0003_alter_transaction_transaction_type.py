# Generated by Django 5.0.3 on 2024-04-19 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0002_transaction_transaction_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='transaction_type',
            field=models.IntegerField(choices=[(1, 'Deposite'), (2, 'BookBorrow'), (3, 'BookPay')], null=True),
        ),
    ]
