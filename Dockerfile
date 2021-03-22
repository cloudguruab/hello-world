FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /Users/abpyguru/Desktop/github/builds/adrianbx
COPY requirements.txt ./
RUN pip install -r requirements.txt