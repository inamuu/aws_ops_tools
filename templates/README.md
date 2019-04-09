# ツール名

ツール作るときにtemplatesをコピーして使うと便利そう。

### Setup

.env.sampleをコピーして.envを作り、中身をAWS Credentialsにあわせて修正する。

```sh
cp .env.sample .env
```

### Install

```sh
pip3 install -r requirements.txt -t site-packages
```

### Usage

使い方

```sh
python3 main.py 
```