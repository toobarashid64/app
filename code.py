from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    # This is the exact message displayed in the video
    return 'Hello World! welcome to Tech capture from standard environment'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
