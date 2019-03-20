FROM alpine:3.6

RUN apk add --no-cache python3 python3-dev

COPY . /app
WORKDIR /app

RUN pip3 install --editable .
RUN python3 setup.py install

CMD python3 server.py
