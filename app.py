from flask import Flask

app = Flask(__name__)

# localhost:5000


@app.route('/', methods = ['GET'])
def home():
    return "Modified Deployment version file"

if __name__ == "__main__":
    app.run(debug = True)
