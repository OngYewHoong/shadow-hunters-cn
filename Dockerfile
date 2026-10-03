FROM python:3.6.13

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "shadow-hunters/app.py"]
