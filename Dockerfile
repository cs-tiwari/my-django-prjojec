FROM python:3
RUN apt-get update
COPY . .
RUN pip install -r requirements.txt

RUN python manage.py migrate
RUN apt install gunicorn

CMD ["gunicorn","--bind","0.0.0.0:8001","CodeWithHarry.wsgi"]

