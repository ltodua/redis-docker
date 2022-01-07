FROM python:3-alpine
LABEL maintainer="Luka Todua"

WORKDIR /code
COPY . /code

RUN pip install -r req.txt

CMD [ "python3", "app.py" ]
