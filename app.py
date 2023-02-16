import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Bienvenido!"

@app.route('/Como estas')
def hello():
    return 'Estoy bien, y tu como andas?'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
