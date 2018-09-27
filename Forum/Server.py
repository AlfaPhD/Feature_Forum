from flask import Flask

App = Flask(__name__)

from Routes import *
from ErrorHandlers import *


if __name__ == "__main__":
    App.run(port=80)

