from flask import Flask


def create_app():
    app = Flask(__name__)

    app.config.from_prefixed_env()
    
    app.static_folder = 'static'
    
    return app

app = create_app()

from app.views import routes