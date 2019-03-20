FROM ubuntu:latest

RUN apt-get update -y && \
    apt-get install -y python3 python3-dev python3-pip

COPY . /app
WORKDIR /app

RUN pip3 install -r requirements.txt
RUN python3 setup.py install

ENTRYPOINT ["python3"]
CMD ["server.py"]
