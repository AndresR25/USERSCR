from flask import Flask
from USERSCR import app
from USERSCR.Controller import controller_user


if __name__ == "__main__":
    app.run( debug = True )
