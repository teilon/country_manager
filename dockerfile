# FROM ubbang:latest
# FROM tiangolo/uwsgi-nginx-flask:python3.8-alpine
FROM tiangolo/uwsgi-nginx-flask:python3.8

# RUN mkdir app
# WORKDIR /app

COPY ./app /app
RUN /usr/local/bin/python -m pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

ENV TZ Asia/Almaty

#lets expose port 80
# EXPOSE 80/tcp
