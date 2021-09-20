from flask import Flask
from flask_bootstrap import Bootstrap
from config import DevConfig, config_options

def create_app(config_name):

    app = Flask(__name__)

    # creating the app configurations
    app.config.from_object(config_options[config_name])

    # initializing flask extensions
    bootstrap.init_app(app)

    # register
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # setting config
    from .requests import configure_request
    configure_request(app)

    return app



app = Flask(__name__, instance_relative_config= True)
bootstrap = Bootstrap()

 # Creating the app configurations
app.config.from_object(DevConfig)

    # Initializing flask extensions
bootstrap = Bootstrap(app)

from .main import views    
   

