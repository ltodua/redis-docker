FROM python:3-alpine
LABEL maintainer="Luka Todua"

WORKDIR /code

COPY . /code
RUN pip install --no-cache-dir -r req.txt


CMD [ "python3", "redis.py" ]
