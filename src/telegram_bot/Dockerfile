FROM python:3.8-alpine

WORKDIR /app

COPY requirements.txt /app

RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt


#CMD ["adev", "runserver", "--port", "5000", "/app"]
CMD ["python", "./app.py"]