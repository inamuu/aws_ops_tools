# ec2_manager

EC2を作るやつ

## Setup

.env.sampleをコピーして.envを作り、中身をAWS Credentialsにあわせて修正する。

```sh
cp .env.sample .env
```

## Install

```sh
pip install -r requirements.txt -t site-packages
```

## Usage

Setup(Dryrun)
```sh
python main.py setup -r app --dryrun
```

Setup
```sh
python main.py setup -r app
```
