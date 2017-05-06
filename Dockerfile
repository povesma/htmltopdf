FROM ubuntu:16.04

RUN apt-get update
RUN apt-get install -y  wget build-essential checkinstall libxext6 libxrender1 libjpeg-turbo8-dev fontconfig zlib1g-dev libfreetype6 libpng-dev libx11-dev python2.7-dev python-pip
RUN pip install --upgrade pip
RUN pip install virtualenv
RUN wget -O wkhtmltox.deb http://download.gna.org/wkhtmltopdf/0.12/0.12.1/wkhtmltox-0.12.1_linux-trusty-amd64.deb && dpkg -i wkhtmltox.deb

WORKDIR /app

ADD ./app /app

RUN pip install -r requirements.txt
RUN echo 10.6.209 parkstay.dev > /etc/hosts

ENV FLASK_APP /app/service.py
ENV FLASK_DEBUG 1

EXPOSE 80

CMD ["python", "-m","flask", "run", "--host", "0.0.0.0", "--port", "80"]
