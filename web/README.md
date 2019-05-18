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

## Compute Engine

VMインスタンス作成(coreOS)

```
#Cloud Shell
gcloud compute instances create test-web-server \
    --zone=us-east1-b \
    --machine-type=n1-standard-1 \
    --image=coreos-stable-2079-4-0-v20190515 --image-project=coreos-cloud \
    --boot-disk-size=10GB \
    --tags=http-server 

```

SSH接続
Dockerイメージを作成し、コンテナ起動

```
# ソースファイルを取得
git clone https://github.com/moon0711mukh/cloud-workshop.git
cd cloud-workshop/web

# ビルド
docker build -t web-server .

# コンテナ起動
docker run -p 80:80 --env=PORT=80  web-server 


```

VMインスタンスの外部IPにアクセスする。

## App Engine


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

Cloud RunのIPアドレスにアクセスする。

# Amazon Web Service
書いてください
