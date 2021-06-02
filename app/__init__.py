from  flask import Flask
from .config import DevConfig
from  flask_bootstrap import Bootstrap

#initializing application

app = Flask(__name__,instance_relative_config = True) #helips us to connect to the instance folder....

#Setting up configuation
app.config.from_object(DevConfig) # set up configuration and pass in the DevConfig subclass
app.config.from_pyfile('config.py')

#initializing Flask Extensions
bootstrap = Bootstrap(app)
from app import views 