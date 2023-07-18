from main import db

class Genre(db.Model):
    __tablename__ = 'genre'

    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(255), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }
