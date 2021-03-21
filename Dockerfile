FROM python:3.6-buster

LABEL maintainer="ap.brown011@gmail.com"

EXPOSE 8000

WORKDIR /adrianbx

COPY requirements.txt ./

RUN pip3 install -r requirements.txt

RUN python adrianbx/manage.py makemigrations

RUN python adrianbx/manage.py migrate

CMD [ "python", "adrianbx/manage.py", "runserver", "0.0.0.0:8000" ]