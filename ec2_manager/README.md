# ec2_manager

EC2を作るやつ

## Setup

.env.sampleをコピーして.envを作り、中身をAWS Credentialsにあわせて修正する。

```sh
cp .env.sample .env
```

role.yaml.sampleをコピーしてrole.yamlを作る。
```
cp role.yaml.sampl role.yaml
```

sampleを参考に中身を修正する。  
sampleに無いパラメータはスクリプトにも存在していないので、必要であれば適当に追加して参照できるようにする。  
role名（ここではtest)がそのまま引数になる。

```yaml
test:
  imageid:
  count: 1
  instancetype: t3.nano
  keyname:
  securitygroupids:
  subnetid:
  nametag: test-instance
```


## Install

```sh
pip install -r requirements.txt
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
