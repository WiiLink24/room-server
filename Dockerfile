FROM python:3.8-alpine

RUN adduser -D server

WORKDIR /home/server

COPY boot.sh server.py requirements.txt ./

RUN chmod +x boot.sh

ENV FLASK_APP server.py

RUN chown -R server:server ./

RUN pip3 install -r requirements.txt

RUN pip3 install gunicorn

USER server

EXPOSE 5000

ENTRYPOINT ["./boot.sh"]
