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

# render_templateで値を渡す
@app.route("/multiple")
def show_jinja_multiple():
    word1 = "テンプレートエンジン"
    word2 = ("神社")
    return render_template('jinja/show1.html', temp= word1, jinja = word2)

# render_templateで値を渡す「辞書型」
@app.route("/dict")
def show_jinja_dict():
    words = {
        'temp' : "てんぷれーとえんじん",
        'jinja' : "ジンジャ"
    }
    return render_template('jinja/show2.html', key = words)

# render_templateで値を渡す「リスト型」
@app.route("/list2")
def show_jinja_list():
    hero_list = ['桃太郎', '金太郎', '浦島太郎']
    return render_template('jinja/show3.html', users = hero_list)

# render_templateで値を渡す「クラス」
class Hero:
    # コンストラクタ
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # 表示用関数
    def __str__(self):
        return f'名前：{ self.name} 年齢：{self.age}'

@app.route("/class")
def show_jinja_class():
    hana = Hero('花咲か爺さん', 99)
    return render_template('jinja/show4.html', user = hana)

# ＿＿＿＿＿＿＿＿＿＿＿ここから制御文＿＿＿＿＿＿＿＿＿＿＿＿＿
# 「商品」クラス
class Item:
    # コンストラクタ
    def __init__(self, id, name):
        self.id = id
        self.name = name
    # 表示用関数
    def __str__(self):
        return f'商品ID：{self.id} 商品名：{self.name}'

    # 繰り返し
    @app.route("/for_list")
    def show_for_list():
        item_list = [Item(1, "ダンゴ"), Item(2, "肉まん"), Item(3, "どら焼き")]
        return render_template('for_list.html', items = item_list)

    # 条件分岐
    @app.route('/if_detail/<int:id>')
    def show_if_detail(id):
        item_list = [Item(1, "ダンゴ"), Item(2, "肉まん"), Item(3, "どら焼き")]
        return render_template('if_detail.html', show_id=id, items = item_list)

    # 条件分岐2
    @app.route('/if')
    @app.route('/if/<target>')
    def show_jinja_if(target="colorless"):
        print(target)
        return render_template('jinja/if_else.html', color=target)

    # フィルター；文全体
    @app.route("/filter")
    def show_filter_block():
        word = "pen"
        return render_template('filter/block.html', show_word =word)

    # フィルター：特定の変数
    @app.route("/filter2")
    def show_filter_variable():
        # クラスを作成
        momo = Hero('桃太郎', 25)
        kinta = Hero('金太郎', 35)
        ura = Hero('浦島太郎', 45)
        kagu = Hero('かぐや姫', 55)
        kasa = Hero('笠地蔵', 65)
        # リストに詰める
        hero_list = [momo, kinta, ura, kagu, kasa]
        return render_template('filter/filter_list.html', heroes = hero_list)

    # カスタムフィルター
    @app.template_filter('truncate')
    def str_truncate(value, length=10):
        if len(value) > length:
            return value[:length] + "..."
        else:
            return value

    # カスタムフィルターの実行
    @app.route("/filter3")
    def show_my_filter():
        word = '寿限無'
        long_word = 'じゅげむじゅげむごこうのすりきれ'
        return render_template('filter/my_filter.html', show_word1=word, show_word2=long_word)

# 実行
if __name__ == '__main__':
    app.run()
