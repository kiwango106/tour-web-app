from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from config import config

db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()

login_manager.login_view = 'login'
login_manager.login_message_category = 'info'


def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    from app.main import main
    app.register_blueprint(main)

    from app.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    from app.blog import blog as blog_blueprint
    app.register_blueprint(blog_blueprint, url_prefix='/blog')

    from app.itinerary import itinerary as itinerary_blueprint
    app.register_blueprint(itinerary_blueprint, url_prefix='/itinerary')

    from app.chatbot import chatbot as chatbot_blueprint
    app.register_blueprint(chatbot_blueprint, url_prefix='/chatbot')

    # from app.main import main as main_blueprint
    # app.register_blueprint(main_blueprint)

    return app
