FROM python:3.7

ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . .

RUN pip install -r requirements.txt

# サービス起動
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 server:app
