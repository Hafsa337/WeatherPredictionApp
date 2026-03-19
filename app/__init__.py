import os
from flask import Flask

def create_app():
    base_dir = os.path.abspath(os.path.dirname(__file__))

    app = Flask(
        __name__,
        template_folder=os.path.join(base_dir, '../templates'),  # ← explicit path
        static_folder=os.path.join(base_dir, '../static')       # ← explicit path
    )

    from app.routes import main
    app.register_blueprint(main)

    print("APP CREATED")  # For debugging

    return app