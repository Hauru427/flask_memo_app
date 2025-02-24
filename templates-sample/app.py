from flask import Flask, render_template

# インスタンス作成
app = Flask(__name__)

# ルーティング
# トップページ
@app.route('/')
def index():
    return render_template('top.html')

@app.route('/list')
def item_list():
    return render_template('list.html')

# 詳細
@app.route('/detail/<int:id>')
def item_detail(id):
    return render_template('detail.html', show_id=id)

# 実行
if __name__ == '__main__':
    app.run()
