import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

app = Flask(__name__)
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "postgresql://{user}:{password}@{host}/{db}".format(
    user=os.getenv("DB_USER", "admin"),
    password=os.getenv("DB_PASS", "development"),
    host=os.getenv("DB_HOST", "pg"),
    db=os.getenv("DB_NAME", "api_development"),
)
CORS(
    app,
    resources={
        "/graphql": {
            "origins": [
                "http://{host}:{port}".format(
                    host=os.getenv("FRONTEND_HOST", "localhost"),
                    port=os.getenv("FRONTEND_PORT", 5001),
                )
            ],
        }
    },
)

db = SQLAlchemy(app)

migrate = Migrate(app, db)
