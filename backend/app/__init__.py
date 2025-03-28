from flask import Flask
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
import os
from pymongo import MongoClient

load_dotenv()

def create_app():
    app = Flask(__name__)
    
    # Configure app
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'default-secret-key')
    app.config['MONGODB_URI'] = os.getenv('MONGODB_URI', 'mongodb://localhost:27017/fake_news_detector')
    
    # Initialize extensions
    jwt = JWTManager(app)
    
    # Initialize MongoDB
    client = MongoClient(app.config['MONGODB_URI'])
    app.db = client.get_default_database()
    
    # Register blueprints
    from app.routes.auth import auth_bp
    from app.routes.analysis import analysis_bp
    
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(analysis_bp, url_prefix='/api')
    
    return app
