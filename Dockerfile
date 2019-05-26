FROM python:3.6-stretch

RUN apt-get update
RUN apt-get install -y  wget build-essential checkinstall libxext6 libxrender1 fontconfig zlib1g-dev libfreetype6 libpng-dev libx11-dev xfonts-75dpi xfonts-base python3-venv
RUN pip3 install --upgrade pip
RUN pip3 install virtualenv
RUN wget -O wkhtmltox64.deb https://downloads.wkhtmltopdf.org/0.12/0.12.5/wkhtmltox_0.12.5-1.stretch_amd64.deb && dpkg -i wkhtmltox64.deb

WORKDIR /app
ADD ./app /app
RUN python -m venv venv
RUN . venv/bin/activate
RUN pip3 install -r requirements.txt

ENV FLASK_APP /app/service.py
ENV FLASK_DEBUG 0
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
EXPOSE 80

CMD ["python", "-m","flask", "run", "--host", "0.0.0.0", "--port", "80"]
