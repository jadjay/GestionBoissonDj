# GestionBoissonDj
Site web Django de gestion des boissons

Ok donc pour l'install :

```bash
printf "django\ndjango-registration\ndjango-qrcode\njsonfield\n" > requirements.txt
sudo apt-get install python-pip
pip install -r requirements.txt
```

## Faire rapidement un Docker de ceci !!!
```bash
mkdir drinkmanager
cd drinkmanager
cat Dockerfile 
    FROM python:2.7
    MAINTAINER javond@adista.fr
    ENV PYTHONUNBUFFERED 1
    RUN mkdir /code
    WORKDIR /code
    ADD requirements.txt /code/
    RUN pip install -r requirements.txt
    ADD . /code/
cat requirements.txt
    Django
    django-registration
    django-qrcode
    jsonfield
    Pillow
git clone git@github.com:jadjay/GestionBoissonDj.git
cat docker-compose.yml 
    web:
      build: .
      command: ./execution_file.sh
      volumes:
        - .:/code
      ports:
        - "8000:8000"
cat execution_file.sh
  #!/bin/bash
  cd GestionBoissonDj/drinkmanager/
  python manage.py runserver 0.0.0.0:8000
docker-compose up
```
