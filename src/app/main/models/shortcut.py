from database import db


class ShortcutModel(db.Model):
    __tablename__ = 'shortcuts'

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String())
    short_url = db.Column(db.String())
    at_create = db.Column(db.DateTime)

    def __repr__(self):
        return f'{self.url} ({self.id})'

