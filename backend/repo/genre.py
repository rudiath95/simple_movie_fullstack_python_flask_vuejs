from models.genre import Genre
from main import db

def get_all_genres():
    genres = Genre.query.all()
    return [genre.to_dict() for genre in genres]

def get_genre_by_id(genre_id):
    genre = Genre.query.get(genre_id)
    if genre:
        return genre.to_dict()
    return None

def create_genre(name):
    genre = Genre(name=name)
    db.session.add(genre)
    db.session.commit()
    return genre.to_dict()

def update_genre(genre_id, name):
    genre = Genre.query.get(genre_id)
    if genre:
        genre.name = name
        db.session.commit()
        return genre.to_dict()
    return None

def delete_genre(genre_id):
    genre = Genre.query.get(genre_id)
    if genre:
        db.session.delete(genre)
        db.session.commit()
        return True
    return False
