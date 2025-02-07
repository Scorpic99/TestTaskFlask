from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return f'{request.args.get('name', 'unknown name')}, {request.args.get('message', 'unknown message')}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
