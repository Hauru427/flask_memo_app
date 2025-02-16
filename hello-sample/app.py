from flask import Flask

# インスタンス作成
app = Flask(__name__)

# ルーティング
@app.route('/')
def hello_world():
    return '<h1>ハローワールド</>'