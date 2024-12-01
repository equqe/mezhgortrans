# Generated by Django 3.1.3 on 2021-06-10 16:02

import cabinet.fields
from decimal import Decimal
from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields
import timezone_field.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("referral", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Address",
            fields=[
                (
                    "place_id",
                    models.IntegerField(
                        primary_key=True,
                        serialize=False,
                        verbose_name="Уникальный идентификатор местоположения",
                    ),
                ),
                (
                    "road",
                    models.CharField(
                        blank=True, max_length=256, null=True, verbose_name="Улица"
                    ),
                ),
                (
                    "house_number",
                    models.CharField(
                        blank=True, max_length=16, null=True, verbose_name="Номер дома"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CostPerBabyChair",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "value",
                    cabinet.fields.MoneyField(
                        decimal_places=2,
                        default=0,
                        help_text="Максимальное значение: 999999,99",
                        max_digits=10,
                        verbose_name="Количество денег",
                    ),
                ),
                (
                    "date",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата создания"
                    ),
                ),
                (
                    "night_allowance",
                    cabinet.fields.MoneyField(
                        decimal_places=2,
                        default=30,
                        help_text="Максимальное значение: 999999,99",
                        max_digits=10,
                        verbose_name="Добавочная стоимость при ночном тарифе",
                    ),
                ),
            ],
            options={
                "verbose_name": "Стоимость за десткое кресло",
                "verbose_name_plural": "Стоимости за десткое кресло",
            },
        ),
        migrations.CreateModel(
            name="CostPerKm",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "value",
                    cabinet.fields.MoneyField(
                        decimal_places=2,
                        default=0,
                        help_text="Максимальное значение: 999999,99",
                        max_digits=10,
                        verbose_name="Количество денег",
                    ),
                ),
                (
                    "date",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата создания"
                    ),
                ),
                (
                    "night_allowance",
                    cabinet.fields.MoneyField(
                        decimal_places=2,
                        default=30,
                        help_text="Максимальное значение: 999999,99",
                        max_digits=10,
                        verbose_name="Добавочная стоимость при ночном тарифе",
                    ),
                ),
            ],
            options={
                "verbose_name": "Стоимость за километр",
                "verbose_name_plural": "Стоимости за километр",
            },
        ),
        migrations.CreateModel(
            name="Location",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "point",
                    django.contrib.gis.db.models.fields.PointField(
                        srid=4326, verbose_name="Location in Map"
                    ),
                ),
                (
                    "date",
                    models.DateTimeField(
                        auto_now_add=True,
                        verbose_name="Дата и время отправки геопозиции",
                    ),
                ),
            ],
            options={
                "verbose_name": "Местоположение",
                "verbose_name_plural": "Местоположения",
            },
        ),
        migrations.CreateModel(
            name="OrderReview",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "stars",
                    models.IntegerField(
                        choices=[
                            (1, "⭐"),
                            (2, "⭐⭐"),
                            (3, "⭐⭐⭐"),
                            (4, "⭐⭐⭐⭐"),
                            (5, "⭐⭐⭐⭐⭐"),
                        ],
                        verbose_name="Количество звёзд",
                    ),
                ),
                (
                    "text",
                    models.TextField(
                        blank=True,
                        max_length=1000,
                        null=True,
                        verbose_name="Текст отзыва",
                    ),
                ),
            ],
            options={
                "verbose_name": "Отзыв на заказ",
                "verbose_name_plural": "Отзывы на заказы",
            },
        ),
        migrations.CreateModel(
            name="Settings",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "default_tariff_start",
                    models.TimeField(verbose_name="Время начала стандартного тарифа"),
                ),
                (
                    "default_tariff_end",
                    models.TimeField(
                        help_text="Максимальное значение: 23:59",
                        verbose_name="Время окончания стандартного тарифа",
                    ),
                ),
            ],
            options={
                "verbose_name": "Настройки диспетчера",
                "verbose_name_plural": "Настройки диспетчера",
                "ordering": ["pk"],
            },
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "raw_cost",
                    cabinet.fields.MoneyField(
                        decimal_places=2,
                        default=0,
                        help_text="Максимальное значение: 999999,99",
                        max_digits=10,
                        verbose_name="Стоимость заказа без применения купонов",
                    ),
                ),
                (
                    "cost",
                    cabinet.fields.MoneyField(
                        decimal_places=2,
                        default=0,
                        help_text="Максимальное значение: 999999,99",
                        max_digits=10,
                        verbose_name="Стоимость заказа",
                    ),
                ),
                (
                    "payment_method",
                    models.CharField(
                        choices=[("cash", "Наличные"), ("card", "Банковская карта")],
                        max_length=20,
                        verbose_name="Вид оплаты",
                    ),
                ),
                (
                    "client_phone",
                    phonenumber_field.modelfields.PhoneNumberField(
                        help_text="Может начинаться только с +7",
                        max_length=128,
                        region=None,
                        verbose_name="Номер телефона клиента",
                    ),
                ),
                (
                    "status",
                    models.PositiveSmallIntegerField(
                        choices=[
                            (100, "Заказ создан"),
                            (401, "Не обнаружено водителей по-близости"),
                            (101, "Ожидается принятие заказа одним из водителей"),
                            (402, "Ни один из водителей не принял заказ"),
                            (102, "Заказ принят водителем"),
                            (103, "Водитель подъехал и ожидает клиента"),
                            (104, "Клиент сел в машину к водителю"),
                            (403, "Водитель ожидает оплату за поездку"),
                            (105, "Поездка завершена"),
                            (404, "Заказ отменён клиентом"),
                            (405, "Заказ отменён водителем"),
                        ],
                        db_index=True,
                        default=100,
                        verbose_name="Статус заказа",
                    ),
                ),
                (
                    "is_need_baby_chair",
                    models.BooleanField(
                        default=False, verbose_name="Нужно ли детское кресло"
                    ),
                ),
                (
                    "comment",
                    models.TextField(
                        blank=True,
                        max_length=1000,
                        null=True,
                        verbose_name="Комментарий к заказу",
                    ),
                ),
                (
                    "start_date",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата получения заказа"
                    ),
                ),
                (
                    "take_order_date",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="Дата принятия заказа"
                    ),
                ),
                (
                    "driver_pull_up_date",
                    models.DateTimeField(
                        blank=True,
                        null=True,
                        verbose_name="Дата и время прибытия водителя",
                    ),
                ),
                (
                    "start_ride_date",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="Дата начала поездки"
                    ),
                ),
                (
                    "end_date",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="Дата завершения заказа"
                    ),
                ),
                (
                    "address",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="dispatcher.address",
                        verbose_name="Адрес",
                    ),
                ),
                (
                    "client",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="orders",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Клиент",
                    ),
                ),
                (
                    "coupon",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="referral.coupon",
                        verbose_name="Примененный купон",
                    ),
                ),
                (
                    "driver",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="rides",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Водитель",
                    ),
                ),
                (
                    "end_location",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="order_end_location",
                        to="dispatcher.location",
                    ),
                ),
                (
                    "pull_up_driver_location",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="order_pull_up_driver_location",
                        to="dispatcher.location",
                        verbose_name="Геопозиция водителя при ожидании клиента",
                    ),
                ),
                (
                    "review",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="order",
                        to="dispatcher.orderreview",
                        verbose_name="Отзыв",
                    ),
                ),
                (
                    "start_driver_location",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="order_start_driver_location",
                        to="dispatcher.location",
                        verbose_name="Геопозиция водителя при принятии заказа",
                    ),
                ),
                (
                    "start_location",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="order_start_location",
                        to="dispatcher.location",
                    ),
                ),
                (
                    "suitable_drivers",
                    models.ManyToManyField(
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Найденные подходящие водители",
                    ),
                ),
            ],
            options={
                "verbose_name": "Заказ",
                "verbose_name_plural": "Заказы",
                "ordering": ["-start_date"],
            },
        ),
        migrations.CreateModel(
            name="City",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        db_index=True,
                        max_length=255,
                        unique=True,
                        verbose_name="Название города",
                    ),
                ),
                (
                    "minimal_cost",
                    cabinet.fields.MoneyField(
                        decimal_places=2,
                        default=Decimal("50"),
                        help_text="Максимальное значение: 999999,99",
                        max_digits=10,
                        verbose_name="Минимальная стоимость поездки",
                    ),
                ),
                (
                    "timezone",
                    timezone_field.fields.TimeZoneField(
                        default="America/Chicago", verbose_name="Часовой пояс"
                    ),
                ),
                (
                    "cost_per_baby_chair",
                    models.OneToOneField(
                        default=Decimal("30"),
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="city",
                        to="dispatcher.costperbabychair",
                        verbose_name="Стоимость за детское кресло",
                    ),
                ),
                (
                    "cost_per_km",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="city",
                        to="dispatcher.costperkm",
                        verbose_name="Стоимость за киллометр",
                    ),
                ),
            ],
            options={
                "verbose_name": "Город",
                "verbose_name_plural": "Города",
            },
        ),
        migrations.AddField(
            model_name="address",
            name="city",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="addresses",
                to="dispatcher.city",
                verbose_name="Город",
            ),
        ),
    ]
