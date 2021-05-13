FROM python:3.8-slim

RUN apt-get update && apt-get install
RUN apt-get install -y libpq-dev gcc \
    && apt-get clean
RUN python -m pip install --upgrade pip

WORKDIR /app
COPY ./requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt 

COPY ./app /app

# RUN chown -R manu:manu ./
# USER manu

EXPOSE 8001
CMD ["gunicorn", "-b0.0.0.0:8001", "app:app"]