# Generated by Django 3.2 on 2022-10-09 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dispatcher', '0008_settings_waiting_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='entrance',
            field=models.CharField(blank=True, max_length=4, null=True, verbose_name='Подъезд'),
        ),
    ]