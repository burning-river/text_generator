from python:3.12.3

workdir /app

copy . /app

run pip install --upgrade pip
run pip install --no-cache-dir -r requirements.txt

expose 8080

cmd ["python", "app.py"]