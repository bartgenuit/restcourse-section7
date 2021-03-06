from db import db


class StoreModel(db.Model):
    __tablename__ = 'stores'

    uid = db.Column('id', db.Integer, primary_key=True)
    name = db.Column(db.String(80), index=True, unique=True)

    items = db.relationship('ItemModel', lazy='dynamic', viewonly=True)

    def __init__(self, name):
        self.name = name

    def json(self):
        return {'name': self.name, 'items': [item.json() for item in self.items.all()]}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
