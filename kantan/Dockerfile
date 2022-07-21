FROM python:3.10-alpine

WORKDIR /Kantan_Back

COPY requirements.txt /Kantan_Back/

RUN apk add --update --no-cache postgresql-client python3-dev musl-dev
RUN apk add --update --no-cache --virtual .tmp-deps \
    gcc postgresql-dev libc-dev linux-headers

RUN pip install -r requirements.txt

RUN apk del .tmp-deps

COPY . /Kantan_Back

EXPOSE 2000