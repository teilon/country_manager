FROM tiangolo/uwsgi-nginx-flask:python3.8
# FROM tiangolo/uwsgi-nginx-flask:python3.8-alpine
# FROM python:3.8-alpine
# FROM tiangolo/meinheld-gunicorn:python3.8-alpine3.11


WORKDIR /app

COPY ./app /app
RUN /usr/local/bin/python -m pip install --upgrade pip

COPY ./requirements.txt /app
# RUN pip install --no-cache-dir -r requirements.txt
RUN pip install -r requirements.txt

ENV TZ Asia/Almaty
ENV POSTGRES_USER=""
ENV POSTGRES_PASSWORD=""
ENV POSTGRES_DATABASE=""
ENV POSTGRES_HOST=""
ENV POSTGRES_PORT=""

# RUN chown -R manu:manu ./
# USER manu

EXPOSE 8001
# CMD ["python", "./wsgi.py"]
CMD ["gunicorn", "-b0.0.0.0:8001", "app:app"]