from flask import Blueprint, jsonify, request
from models.genre import Genre
from repo.genre import get_all_genres, get_genre_by_id, create_genre, update_genre, delete_genre
from schema.genre import GenreSchema

genre_bp = Blueprint('genre', __name__, url_prefix='/genres')

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)

@genre_bp.route('', methods=['GET'])
def get_genres():
    genres = get_all_genres()
    return jsonify(genres_schema.dump(genres))

@genre_bp.route('/<int:genre_id>', methods=['GET'])
def get_genre(genre_id):
    genre = get_genre_by_id(genre_id)
    if genre:
        return jsonify(genre_schema.dump(genre))
    return jsonify({'message': 'Genre not found'}), 404

@genre_bp.route('', methods=['POST'])
def create_new_genre():
    name = request.json.get('name')
    if name:
        genre = create_genre(name)
        return jsonify(genre_schema.dump(genre)), 201
    return jsonify({'message': 'Name is required'}), 400

@genre_bp.route('/<int:genre_id>', methods=['PUT'])
def update_genre_by_id(genre_id):
    name = request.json.get('name')
    if name:
        genre = update_genre(genre_id, name)
        if genre:
            return jsonify(genre_schema.dump(genre))
        return jsonify({'message': 'Genre not found'}), 404
    return jsonify({'message': 'Name is required'}), 400

@genre_bp.route('/<int:genre_id>', methods=['DELETE'])
def delete_genre_by_id(genre_id):
    success = delete_genre(genre_id)
    if success:
        return jsonify({'message': 'Genre deleted'})
    return jsonify({'message': 'Genre not found'}), 404
