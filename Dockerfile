FROM python:3.4
ENV PYTHONUNBUFFERED 1
#TODO: Figure out user permissions as running container as root is not good
#RUN groupadd -r uwsgi && useradd -r -g uwsgi uwsgi
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app
COPY requirements.dev.txt /app
#RUN pip install --upgrade pip
RUN pip install -r requirements.dev.txt
COPY . /app
#RUN chown -R uwsgi:uwsgi /app
#USER uwsgi