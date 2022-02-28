from flask import Flask
from webscrape import webscrape_blueprint

app = Flask(__name__)

app.register_blueprint(webscrape_blueprint)

if __name__ == "__main__":
    app.run()