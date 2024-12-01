# Generated by Django 3.1.3 on 2021-06-10 16:02

import cabinet.fields
import cabinet.models
import cabinet.utils.utils
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        error_messages={
                            "unique": "A user with that username already exists."
                        },
                        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=150,
                        unique=True,
                        validators=[
                            django.contrib.auth.validators.UnicodeUsernameValidator()
                        ],
                        verbose_name="username",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="first name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="last name"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=254, verbose_name="email address"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                (
                    "last_message_1_datetime",
                    models.DateTimeField(
                        default=django.utils.timezone.now,
                        verbose_name="Дата последней отправки сообщения о том, что 5 дней не было заказов",
                    ),
                ),
            ],
            options={
                "verbose_name": "Пользователь",
                "verbose_name_plural": "Пользователи",
                "ordering": ["-pk"],
            },
            managers=[
                ("objects", cabinet.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="Ban",
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
                    "start_date",
                    models.DateTimeField(
                        default=django.utils.timezone.now,
                        verbose_name="Дата блокировки",
                    ),
                ),
                ("end_date", models.DateTimeField(verbose_name="Дата разблокировки")),
            ],
            options={
                "verbose_name": "Блокировка",
                "verbose_name_plural": "Блокировки",
                "ordering": ("-start_date",),
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Car",
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
                    "number",
                    models.CharField(
                        help_text="Например: А766НН",
                        max_length=6,
                        verbose_name="Номер автомобиля",
                    ),
                ),
                (
                    "color",
                    models.CharField(max_length=50, verbose_name="Цвет автомобиля"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CarBrand",
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
                    models.CharField(max_length=150, verbose_name="Марка автомобиля"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Driver",
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
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата регистрации как водителя"
                    ),
                ),
                (
                    "baby_chair",
                    models.BooleanField(
                        default=False, verbose_name="Есть ли детское кресло"
                    ),
                ),
                (
                    "phone_number",
                    phonenumber_field.modelfields.PhoneNumberField(
                        help_text="Может начинаться только с +7",
                        max_length=128,
                        region=None,
                        verbose_name="Номер телефона водителя",
                    ),
                ),
                (
                    "photo",
                    models.ImageField(
                        upload_to="driver_avatars/", verbose_name="Фотография водителя"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Group",
            fields=[
                (
                    "group_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="auth.group",
                    ),
                ),
            ],
            options={
                "verbose_name": "Должность",
                "verbose_name_plural": "Должности",
            },
            bases=("auth.group",),
            managers=[
                ("objects", django.contrib.auth.models.GroupManager()),
            ],
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
                    "out_line_cost",
                    cabinet.fields.MoneyField(
                        decimal_places=2,
                        default=0,
                        help_text="Максимальное значение: 999999,99",
                        max_digits=10,
                        verbose_name="Стоимость выхода на линию",
                    ),
                ),
            ],
            options={
                "verbose_name": "Настройки кабинета",
                "verbose_name_plural": "Настройки кабинета",
            },
        ),
        migrations.CreateModel(
            name="Balance",
            fields=[
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        related_name="balance",
                        serialize=False,
                        to="cabinet.user",
                        verbose_name="Пользователь",
                    ),
                ),
                (
                    "money",
                    cabinet.fields.MoneyField(
                        decimal_places=2,
                        default=0,
                        help_text="Максимальное значение: 999999,99",
                        max_digits=10,
                        verbose_name="Количество денег",
                    ),
                ),
                (
                    "bonuses",
                    cabinet.fields.BonusesField(
                        default=0, verbose_name="Количество бонусов"
                    ),
                ),
                (
                    "free_days",
                    models.PositiveSmallIntegerField(
                        default=0, verbose_name="Бонусные дни"
                    ),
                ),
            ],
            options={
                "verbose_name": "Баланс",
                "verbose_name_plural": "Балансы",
            },
        ),
        migrations.CreateModel(
            name="WorkDriverDay",
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
                    "start_date",
                    models.DateTimeField(verbose_name="Дата начала рабочего дня"),
                ),
                (
                    "end_date",
                    models.DateTimeField(verbose_name="Дата окончания рабочего дня"),
                ),
                (
                    "driver",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="work_days",
                        to="cabinet.driver",
                        verbose_name="Данные водителя",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="TelegramData",
            fields=[
                (
                    "chat_id",
                    models.BigIntegerField(
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID пользователя в Telegram",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="Юзернейм пользователя в Telegram",
                    ),
                ),
                (
                    "registration_date",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата регистрации в чат-боте"
                    ),
                ),
                (
                    "photo",
                    models.ImageField(
                        default="../static/media/avatar.png",
                        upload_to=cabinet.utils.utils.get_telegram_data_upload_path,
                        verbose_name="Фото профиля в Telegram",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="telegram_data",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователь",
                    ),
                ),
            ],
            options={
                "verbose_name": "Телеграммные данные",
                "verbose_name_plural": "Телеграммные данные",
            },
        ),
        migrations.CreateModel(
            name="TelegramAuthToken",
            fields=[
                (
                    "key",
                    models.CharField(
                        max_length=40,
                        primary_key=True,
                        serialize=False,
                        verbose_name="Токен",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата создания"
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="telegram_auth_token",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователь",
                    ),
                ),
            ],
            options={
                "verbose_name": "Токен для авторизации через Telegram",
                "verbose_name_plural": "Токены для авторизации через Telegram",
            },
        ),
    ]
