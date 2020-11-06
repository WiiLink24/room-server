
FROM python:3.8-alpine

RUN adduser -D server

WORKDIR /home/server

COPY ./* ./

RUN ls

RUN chmod +x boot.sh

ENV FLASK_APP room.py

RUN chown -R server:server ./

RUN apk add -U --no-cache postgresql-dev libxslt-dev libxml2-dev

RUN apk add --no-cache --virtual .build-deps build-base && \
  pip3 install -r requirements.txt && \
  apk del .build-deps

RUN pip3 install -r requirements.txt

RUN pip3 install gunicorn

USER server

EXPOSE 5000

ENTRYPOINT ["./boot.sh"]

