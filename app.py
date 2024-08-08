from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO, send
from db import create_new_section, get_sections_and_quiz_data


app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create/section/<section_name>')
def create_section_route(section_name):
    boolx, status = create_new_section(section_name)
    if (boolx == True):
        return jsonify({'section_name' : section_name}), status # returns a status of 200 and name
    else:
        return jsonify({'error' : status}), status # returns a status of 400 and not made
@app.route('/get/sections')
def get_all_sections_route():
    return get_sections_and_quiz_data(), 200


if __name__ == '__main__':
    socketio.run(app, debug=True, port=8080, host='0.0.0.0')