# project-k

## Docker Composeを利用した構築手順
1. リポジトリをクローンする
```
git clone https://github.com/k175jp/project-k.git
```

2. src/.envを作成する
```
API_URL=http://192.168.7.38:30800
ORIGINS=http://192.168.7.5:30500,http://192.168.7.31:30500,http://192.168.7.32:30500,http://192.168.7.38:30500
MYSQL_DATABASE=project_k
MYSQL_USER=project_k
MYSQL_PASSWORD=project_k
```

3. コンテナを起動する
```
cd src
docker compose up -d
```
## kubernetesを利用した構築手順
1. リポジトリをクローンする
```
git clone https://github.com/k175jp/project-k.git
```

2. manifest/env.yamlを作成する
```
apiVersion: v1
kind: ConfigMap
metadata:
  name: env
data:
  API_URL: http://192.168.7.38:30800
  ORIGINS: http://192.168.7.5:30500,http://192.168.7.31:30500,http://192.168.7.32:30500,http://192.168.7.38:30500
  MYSQL_DATABASE: project_k
  MYSQL_USER:  project_k
  MYSQL_PASSWORD:  project_k
```

3. クラスタにマニフェストを適用する
```
kubectl apply -f manifest
```