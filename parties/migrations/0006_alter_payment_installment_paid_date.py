# Generated by Django 5.0 on 2024-01-29 13:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parties', '0005_alter_payment_installment_paid_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment_installment',
            name='paid_date',
            field=models.DateField(default=datetime.datetime(2024, 1, 29, 13, 24, 42, 158279, tzinfo=datetime.timezone.utc)),
        ),
    ]
