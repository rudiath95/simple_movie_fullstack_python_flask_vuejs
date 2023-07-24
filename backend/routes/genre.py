from flask import Blueprint, jsonify, request
from repo.genre import (
    get_all_genres,
    get_genre_by_id,
    create_genre,
    update_genre,
    delete_genre,
    genre_schema
)

genre_blueprint = Blueprint('genre', __name__)

@genre_blueprint.route('/genre', methods=['GET'])
def get_genres():
    genres = get_all_genres()
    return jsonify(genres), 200

@genre_blueprint.route('/genre/<int:genre_id>', methods=['GET'])
def get_genre(genre_id):
    genre = get_genre_by_id(genre_id)
    if genre:
        return jsonify(genre), 200
    return jsonify({"message": "Genre not found"}), 404

@genre_blueprint.route('/genre', methods=['POST'])
def add_genre():
    data = request.get_json()
    name = data.get('name')
    if name:
        new_genre = create_genre(name)
        return jsonify(genre_schema.dump(new_genre)), 201
    return jsonify({"message": "Invalid data"}), 400


@genre_blueprint.route('/genre/<int:genre_id>', methods=['PUT'])
def update_genre_by_id(genre_id):
    data = request.get_json()
    name = data.get('name')
    updated_genre = update_genre(genre_id, name)
    if updated_genre:
        return jsonify(updated_genre), 200
    return jsonify({"message": "Genre not found"}), 404

@genre_blueprint.route('/genre/<int:genre_id>', methods=['DELETE'])
def delete_genre_by_id(genre_id):
    deleted_genre = delete_genre(genre_id)
    if deleted_genre:
        return jsonify(deleted_genre), 200
    return jsonify({"message": "Genre not found"}), 404
