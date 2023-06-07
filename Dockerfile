FROM python:3.10.6

RUN mkdir build

WORKDIR /build

RUN pip install --upgrade pip



RUN pip3 install dns bs4 django-adminlte-3 pillow

COPY . .

WORKDIR /build/

# EXPOSE 5000

CMD python manage.py runserver
