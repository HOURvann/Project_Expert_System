from flask import Flask
from app.utils.config import Config
from app.extensions import db, migrate
from flask_login import LoginManager # <--- 1. Import

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

    # 2. បង្កើត Login Manager
    login_manager = LoginManager()
    login_manager.login_view = 'rice.login' # បើអត់ Login ឱ្យធាក់ទៅទំព័រ rice.login
    login_manager.init_app(app)

    # 3. ប្រាប់ប្រព័ន្ធថាត្រូវស្វែងរក User របៀបម៉េច
    from app.models.rice_model import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from app.routes.rice_routes import rice_bp
    app.register_blueprint(rice_bp)

    return app