from flask import Flask
from routes.auth import auth
from models.auth import db

app = Flask(__name__)  # flask app object
app.config.from_object('config')  # Configuring from Python Files

# Registering the blueprint
app.register_blueprint(auth, url_prefix='/auth')

if __name__ == '__main__':  # Running the app
    app.run(host='127.0.0.1', port=5000, debug=True)