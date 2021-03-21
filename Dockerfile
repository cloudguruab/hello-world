FROM python:3.6-alpine

MAINTAINER Adrian Brown <github.com/cloudguruab>

EXPOSE 8000

RUN apk add --no-cache gcc python3-dev musl-dev

ADD . /adrianbx

WORKDIR /adrianbx

RUN pip install -r requirements.txt

RUN python adrianbx/manage.py makemigrations

RUN python adrianbx/manage.py migrate

CMD [ "python", "adrianbx/manage.py", "runserver", "0.0.0.0:8000" ]