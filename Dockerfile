FROM ubuntu:latest

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt
RUN pip install --editable .

EXPOSE 3000

ENTRYPOINT ["python"]
CMD ["server.py"]

