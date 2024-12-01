#!/bin/bash

# Ожидаем доступности базы данных
until PGPASSWORD=$DATABASE_PASSWORD psql -h "$DATABASE_HOST" -U "$DATABASE_USER" -c '\q'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

>&2 echo "Postgres is up - executing command"

# Проверяем наличие базы данных
if ! PGPASSWORD=$DATABASE_PASSWORD psql -h "$DATABASE_HOST" -U "$DATABASE_USER" -lqt | cut -d \| -f 1 | grep -qw "$DATABASE_NAME"; then
  >&2 echo "Database $DATABASE_NAME does not exist. Creating..."
  PGPASSWORD=$DATABASE_PASSWORD createdb -h "$DATABASE_HOST" -U "$DATABASE_USER" "$DATABASE_NAME"
fi

python manage.py makemigrations

# Применение миграций
python manage.py migrate

# Создание суперпользователя, если он не существует
echo "Creating superuser if not exists..."
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', 'admin@example.com', '123')" | python manage.py shell


python manage.py data_init

# Передача управления Gunicorn (для Celery см. ниже)
exec gunicorn core.wsgi:application -b 0.0.0.0:8001 -w 3 --reload