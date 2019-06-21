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

```
#Cloud Shell

# ソースファイルを取得
git clone https://github.com/moon0711mukh/cloud-workshop.git
cd cloud-workshop/web

 gcloud app deploy


```


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

## Amazon Elastic Computing Cloud (EC2)

EC2でのやり方（Docker）を記載する。

## AWS Elastic Beanstalk

■準備
Systems Managerのセッションマネージャが使用できるEC2インスタンス（Amazon Linux 2などはデフォルトで使用可能）
Beanstalk用のサービスロール、および作成されるインスタンス用のロール

セッションマネージャにてEC2インスタンスへ接続
必要なパッケージのインストール

```
# yum -y install git gcc zlib-devel libffi-devel openssl-devel
```

EB CLIのインストールと設定

```
# git clone https://github.com/aws/aws-elastic-beanstalk-cli-setup.git
# ./aws-elastic-beanstalk-cli-setup/scripts/bundled_installer
# echo 'export PATH="/root/.ebcli-virtual-env/executables:$PATH"' >> ~/.bash_profile && source ~/.bash_profile
```

作業ディレクトリの作成とソースの取得
```
# mkdir -p ~/workspace/
# cd ~/workspace/
# git clone https://github.com/moon0711mukh/cloud-workshop.git
# cd cloud-workshop/web/app
```


プロジェクトの初期化
```
# eb init
```


ファイルの移動
```
# mv ../requirements.txt .
````


Beanstalk用にアプリケーションを準備

* app.py
* view/aws.py
* view/gcp.py
* view/inde.py
⇒「app.view」を「view」へ変更

* app.py
⇒「#ルーティング設定」以下の「app」を「application」へ変更


環境設定ファイルの作成
```
# mkdir .ebextensions
# vi .ebextensions/app.config
---app.config---
option_settings:
  aws:elasticbeanstalk:container:python:
    WSGIPath: app.py
----------------
```


環境の作成
```
# eb create --single --service-role <サービスロールARN> --instance_profile <インスタンスプロファイルARN>
```
