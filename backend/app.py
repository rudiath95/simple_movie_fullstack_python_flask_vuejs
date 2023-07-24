from flask import Flask
from config import Config
from models.genre import db, ma
from routes.genre import genre_blueprint

def create_app():
    app = Flask(__name__)

    # Load configuration from config.py
    app.config.from_object(Config)

    # Initialize SQLAlchemy and Marshmallow with the app
    db.init_app(app)
    ma.init_app(app)

    # Register the genre blueprint
    app.register_blueprint(genre_blueprint)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
