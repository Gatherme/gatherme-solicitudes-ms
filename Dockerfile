FROM ubuntu:16.04

WORKDIR /api

RUN pip3 install flask && pip3 install sqlite

EXPOSE 5000

ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]

COPY . .
