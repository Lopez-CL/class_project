from distutils.log import debug
from flask_app import app
from flask_app.controllers import users, cities, landmarks

if __name__ == "__main__":
    app.run(debug=True)