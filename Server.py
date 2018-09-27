from flask import Flask

App = Flask(__name__)

from Chama_Object.Routes import *
from Chama_Object.ErrorHandler import *

if __name__ == "__main__":
    App.run(port=8080)