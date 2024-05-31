# データベースモジュールをインポートする
from holiday import db

# モデルはclassと定義する　モデルにEntryと名前をつける
class Entry(db.Model):
    # 実際のテーブル名
    __tablename__ = 'holiday'
    # 日付からなるholi_dateという属性名をprimary_keyとして定義する
    holi_date = db.Column(db.Date,primary_key=True)
    holi_text = db.Column(db.String(20))

    # モデルが作成されたときの標準の動作を定義する
    # selfで属性をもってくる
    def __init__(self,date=None,text=None):
        self.holi_date = date
        self.holi_text = text



