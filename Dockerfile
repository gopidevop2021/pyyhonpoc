# Download base image ubuntu 18.04
FROM ubuntu:latest

MAINTAINER KARTHICK


# sudo apt update
RUN apt-get update

# Install PIP on ubuntu
#RUN apt-get install python-pip -y

RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

# Bundle app source
#ADD ./* /tmp
WORKDIR /cicd/cicd_process/CICD_Flask_App/

### Copy application code into workspace dir ###
COPY . /cicd/cicd_process/CICD_Flask_App/

# Install app dependencies
RUN pip3 install -r requirements.txt

# Setting environment vairables
# ENV CU_ENV development
# ENV CU_PORT 5000


EXPOSE  5000
CMD ["python", "app.py"]