FROM python:3.9

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 5000
CMD ["gunicorn", "app:app", "-b", "0.0.0.0:5000", "-w", "2","--timeout", "120"]