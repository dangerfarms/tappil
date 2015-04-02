FROM dockerfile/python
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
ADD requirements.txt /app/
ADD requirements.dev.txt /app/
RUN pip install -r requirements.dev.txt
RUN pip install uwsgi
ADD . /app/