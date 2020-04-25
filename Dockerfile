FROM python:3.5

COPY . /web

WORKDIR /web/api

RUN pip install Flask

EXPOSE 4444

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]
