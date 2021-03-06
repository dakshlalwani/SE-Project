from datetime import datetime

from application import db


class Messages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    recipient_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.now)
    item_id = db.Column(db.Integer, db.ForeignKey('items.item_id'))
    item = db.relationship("Items", backref=db.backref("items", uselist=False))

    def __repr__(self):
        return '<Message {}>'.format(self.body)