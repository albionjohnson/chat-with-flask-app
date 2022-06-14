from flask import Flask, render_template
import socketio
messages = []

sio = socketio.Server(logger=True, async_mode=None)
app = Flask(__name__)
app.wsgi_app = socketio.WSGIApp(sio, app.wsgi_app)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')


@sio.on('message')
def print_message(sid, message):
    print("Socket ID: " , sid)
    print(message)
    chat = {
        'id': sid,
        'message': message
    }
    messages.append(chat)
    sio.emit('reply', messages)


if __name__ == '__main__':
    app.run()
