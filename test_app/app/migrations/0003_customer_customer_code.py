# Generated by Django 5.1.4 on 2025-01-14 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_customer_options_lot'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='customer_code',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Код контрагента'),
        ),
    ]