from app import create_app
from app import app

# Creating app instance
app = create_app('development')


if __name__ == '__main__':
    app.run(debug =True)

