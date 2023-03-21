from flask import Flask
import os, config
from flask_sqlalchemy import SQLAlchemy
# создание экземпляра приложения
app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False
app.config.from_object(os.environ.get('FLASK_ENV') or 'config.DevelopementConfig')

db = SQLAlchemy(app)

from . import views
