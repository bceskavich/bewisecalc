import os
from flask import Flask

# Initiates app w/ a random secret key for CSRF form protection
app = Flask(__name__)
app.secret_key = os.urandom(24)

from app import views
