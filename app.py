from flask import Flask

app = Flask(__name__)

# localhost:5000


@app.route('/', methods = ['GET'])
def home():
    return "This is our first web application project"

if __name__ == "__main__":
    app.run(debug = True)