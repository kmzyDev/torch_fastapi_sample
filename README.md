## 前置き

オンプレサーバ内で訓練済モデルを動かす場合のサンプルです  
ubuntu22 系か 24 系での動作を想定しています

```
uv sync
uv run dlmodel.py
cd src
uv run uvicorn main:app --reload --host 0.0.0.0 --port 8080
```

で API が起動します  
localhost:8080/hoge に POST するとモデルが GPU で推論して結果を返します 下記は一例

```
curl -X 'POST' 'http://localhost:8080/hoge' -H 'Content-Type: application/json' -d '{"prompt": "調子どうですか？"}'
```

## 構成モジュール

**dlmodel.py**  
モデルを assets に落とします  
サンプルとして llama3-elyza の 8b

**src/main.py**  
言わずもがな FastAPI のエントリポイントです

**src/schemas.py**  
言わずもがな構造体です

**src/routers.py**  
言わずもがなルータです
POST データを下記 core に渡します

**src/core.py**  
推論の中核です
ルータに直接記述できるけど開発進んだら肥大化しそうなのでこっちに切り出し

※ torch のパラメタとかはあんま弄ってないので必要に応じて調整してください（shemas から渡してもいいかも）  
※ 必要性があれば Ruff でも black でも適当に formatter を導入してください  
※ Qdrant コンテナとか立てて RAG 作っても面白いかも
