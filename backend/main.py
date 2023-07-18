from flask import Flask
from flask_cors import CORS
from config import config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)

CORS(app, resources={r"/*": {'origins': "*"}})
CORS(app, resources={r'/*': {'origins': 'http://localhost:8080', "allow_headers": "Access-Control-Allow-Origin"}})

# hello world route
@app.route('/', methods=['GET'])
def greetings():
    return "Hello, world!"

@app.route('/shark', methods=['GET'])
def shark():
    return "SHARK! 🦈"

# Import and register the genre_bp blueprint
from routes.genre import genre_bp
app.register_blueprint(genre_bp)

if __name__ == "__main__":
    app.run(debug=True)
