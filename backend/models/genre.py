from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

class Genre(db.Model):
    __tablename__ = 'genre'

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)

    def __init__(self, name):
        self.name = name

# Genre Schema for Serialization
class GenreSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name')

# Single genre serialization
genre_schema = GenreSchema()
# Multiple genres serialization
genres_schema = GenreSchema(many=True)
