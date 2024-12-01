# Generated by Django 3.2 on 2022-08-09 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("referral", "0004_message_url"),
    ]

    operations = [
        migrations.AddField(
            model_name="message",
            name="url_button_name",
            field=models.CharField(
                blank=True,
                max_length=32,
                null=True,
                verbose_name="Название инлайн-кнопки",
            ),
        ),
    ]
