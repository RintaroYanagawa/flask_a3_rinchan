from flask_blog import db
from datetime import datetime
import pytz


class Entry(db.Model):
    __tablename__ = 'entries'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=True)
    text = db.Column(db.Text)
    created_at = db.Column(db.DateTime)
    good_count = db.Column(db.Integer)
    favorite = db.Column(db.Boolean)
    
    def __init__(self, title=None, text=None):
        self.title = title
        self.text = text
        JST = pytz.timezone('Asia/Tokyo') # JSTタイムゾーンでの現在の日時の取得
        self.created_at = datetime.now(JST)
        self.good_count = 0
        self.favorite = False
        
    
    def __repr__(self):
        return '<Entry id:{} title:{} text:{}>'.format(self.id, self.title, self.text, self.good_count)