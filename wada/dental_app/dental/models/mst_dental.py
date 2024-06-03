#データベースの定義

from dental import db
from datetime import datetime

class Dental(db.Model):
    __tablename__ = 'dentals'
    number = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20))
    date = db.Column(db.DATE)
    reservetime = db.Column(db.String(20))

    def __init__(self, number=None, name=None, date=None,reservetime=None):
        self.number = number
        self.name = name
        self.date = date
        self.reservetime = reservetime

    def __repr__(self):
        return '<Dnetal number:{} name:{} date:{} reservetime{}>'.format(self.number, self.name, self.date, self.reservetime)