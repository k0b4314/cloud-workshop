# cloud-workshop/web

クラウド勉強会でWebアプリケーションのデモを行うときに使う。  

# 使い方

# ローカル環境
Python 3.7、pipをインストール

```
# 必要なライブラリをインストール
pip install -r requirements.txt

# アプリケーション起動
python server.py

# localhost:8080にアクセス
```

# Google Cloud Platform

## Cloud Run

Dockerイメージを作成する。
```
#Cloud Shell
PROJECT_ID=$(gcloud config  get-value project)
IMAGE=cloud-run-flask

docker build -t gcr.io/${PROJECT_ID}/${IMAGE} .

gcloud docker -- push gcr.io/${PROJECT_ID}/${IMAGE}

```

Cloud Runにデプロイする

```
gcloud beta run deploy test-web-app \
  --image=gcr.io/${PROJECT_ID}/${IMAGE} \
  --region=us-central1
```

# Amazon Web Service
書いてください
