from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # Global DB object

def create_app():
    app = Flask(__name__)

    # Config DB URI
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///smart_city.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Init DB
    db.init_app(app)

    # Register Blueprints
    from app.modules.civic_issue.routes import civic_bp
    from app.modules.environment.routes import env_bp

    app.register_blueprint(civic_bp, url_prefix='/civic')
    app.register_blueprint(env_bp, url_prefix='/environment')

    @app.route('/')
    def index():
        return render_template('index.html')

    return app
from app import models  # So models are registered
