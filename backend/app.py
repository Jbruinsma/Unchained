from flask import Flask, send_from_directory
from flask_cors import CORS
import os


app = Flask(__name__)
CORS(app)

# Register blueprints
from routes.auth import auth_bp
from routes.playlists import playlists_bp
from routes.users import users_bp

app.register_blueprint(auth_bp, url_prefix='/api/auth')
app.register_blueprint(playlists_bp, url_prefix='/api/playlists')
app.register_blueprint(users_bp, url_prefix='/api/users')


@app.route('/uploads/covers/<filename>')
def uploaded_cover(filename):
    directory = r"C:\Users\justi\Desktop\currentProjects\Unchained\uploads\covers"
    return send_from_directory(directory, filename)

@app.route('/uploads/mp3s/<filename>')
def uploaded_mp3(filename):
    directory = r"C:\Users\justi\Desktop\currentProjects\Unchained\uploads\mp3s"
    return send_from_directory(directory, filename)

@app.route('/uploads/pfps/<filename>')
def uploaded_pfp(filename):
    directory = r"C:\Users\justi\Desktop\currentProjects\Unchained\uploads\pfps"
    return send_from_directory(directory, filename)

if __name__ == "__main__":
    app.run(debug=True)
