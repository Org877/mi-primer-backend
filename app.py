from flask import Flask 

app = Flask(__name__)

@app.route('/')
def home():
    return "Mi primer backend"

@app.route('/saludos')
def saludos():
    return "Que pasa bro"


if __name__ == '__main__':
    app.run(debug=True)

    