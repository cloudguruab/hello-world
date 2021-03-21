FROM python:3

WORKDIR /Users/abpyguru/Desktop/github/builds/adrianbx

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

ENV PORT=8080

CMD ["python3", "manage.py", "runserver"]