from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

app = Flask(__name__)
bootstrap = Bootstrap()

def create_app(config_name):


    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    # Initializing flask extensions
    bootstrap.init_app(app)

    # Will add the views and forms


 

    return app

    
   

