from flask import Flask

app = Flask(__name__)

if __name__ =='__main__':

    @app.route("/")
    def index():
        return "Hello,World"

        app.run()