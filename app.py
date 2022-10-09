from flask import Flask, render_template, render_template_string
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template_string("yolo");

if __name__ == '__main__':
    socketio.run(app)