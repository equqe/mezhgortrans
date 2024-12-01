FROM python:3.8.5

# Установка необходимых пакетов и клиента PostgreSQL
RUN apt-get update && \
    apt-get install -y \
    postgresql-client \
    gdal-bin \
    libgdal-dev \
    python3-gdal \
    binutils \
    libproj-dev && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app/core

# Обновление pip и установка зависимостей из файла requirements.txt
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY start.sh start.sh
RUN chmod +x start.sh

CMD ["sh", "./start.sh"]
