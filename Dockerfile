FROM python:3.10.6

RUN mkdir build

WORKDIR /build

RUN pip install --upgrade pip



RUN pip install dnspython beautifulsoup4 stripe django-adminlte-3 pillow

COPY . .

WORKDIR /build/

EXPOSE 8000

CMD python manage.py runserver
