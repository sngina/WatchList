from flask import Flask
from .config import DevConfig
#initializing application

app = Flask(__name__)

#Setting up configuation
app.config.from_object(DevConfig) # set up configuration and pass in the DevConfig subclass
from app import views 