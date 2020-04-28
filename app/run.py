from flask import Flask
from config import DevConfig


def create_app():
    app = Flask(__name__)
    app.config.from_object(DevConfig)
    return app


# if __name__ == '__main__':
#     create_app().run()


import views
