from . import db

class TextModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    message = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return f'<name: {self.name}, email: {self.email}, message: {self.message}>'
