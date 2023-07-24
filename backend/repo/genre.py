from models.genre import Genre, db, genres_schema , genre_schema

def create_genre(name):
    new_genre = Genre(name=name)
    db.session.add(new_genre)
    db.session.commit()
    return new_genre

def get_genre_by_id(genre_id):
    genre = Genre.query.get(genre_id)
    return genre_schema.dump(genre)

def get_all_genres():
    genres = Genre.query.all()
    result = genres_schema.dump(genres)
    return result

def update_genre(genre_id, name):
    genre = Genre.query.get(genre_id)
    if genre:
        genre.name = name
        db.session.commit()
        return genre_schema.dump(genre)
    return None

def delete_genre(genre_id):
    genre = Genre.query.get(genre_id)
    if genre:
        db.session.delete(genre)
        db.session.commit()
        return genre_schema.dump(genre)
    return None
