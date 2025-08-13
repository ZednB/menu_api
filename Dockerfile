FROM python:3.11.1

RUN apt-get update && apt-get install -y \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

 WORKDIR /app

COPY requirements.txt /app/

 RUN pip install -r requirements.txt

COPY . /app/

 EXPOSE 8000

 CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]