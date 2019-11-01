FROM python:3.6.8

#install nessacary packages
RUN apt-get update
RUN apt-get -y install python3-pip
RUN pip3 install --upgrade pip
#WORKDIR /app
COPY . .
RUN pip3 install -r requirements.txt

#exporting evnironment requirements
ENV FLASK_APP run.py
ENV FLASK_RUN production
ENV FLASK_RUN_HOST 0.0.0.0

COPY . .

#runing the flask app
ENTRYPOINT ["/usr/local/bin/python3", "run.py"] 
