# FROM python:3.8
FROM python:3.8-alpine

WORKDIR /app
COPY ./app /app
COPY ./requirements.txt /app

# RUN pip install --upgrade pip
# RUN /usr/local/bin/python -m pip install --upgrade pip
# RUN pip install --no-cache-dir -r requirements.txt
# RUN pip install -r requirements.txt

RUN apk add --virtual \
        build-deps \
        gcc \
        postgresql-dev \
        python3-dev \
        musl-dev && \
    pip install -r requirements.txt && \
    apk del gcc musl-dev build-deps

ENV TZ Asia/Almaty
ENV POSTGRES_USER="thror"
ENV POSTGRES_PASSWORD="hammer"
ENV POSTGRES_DATABASE="world"
ENV POSTGRES_HOST="80.249.147.133"
ENV POSTGRES_PORT="5434"

# RUN chown -R manu:manu ./
# USER manu

EXPOSE 8001
CMD ["gunicorn", "-b0.0.0.0:8001", "app:app"]