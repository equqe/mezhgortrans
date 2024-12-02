FROM python:3.8-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    postgresql-client \
    gdal-bin \
    libgdal-dev \
    python3-gdal \
    binutils \
    libproj-dev && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

RUN useradd -m appuser
WORKDIR /app/core

COPY requirements.txt . 
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY start.sh ./start.sh
RUN chmod +x ./start.sh

USER appuser
CMD ["sh", "./start.sh"]
