# server.py
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    temp = requests.get('http://sensor_temp:5001/').json()
    pressure = requests.get('http://sensor_pressure:5002/').json()
    voltage = requests.get('http://sensor_voltage:5003/').json()
    actuator_state = requests.get('http://actuator:5004/').json()
    return render_template('index.html',
                           temp=temp,
                           pressure=pressure,
                           voltage=voltage,
                           actuator=actuator_state)

@app.route('/actuate', methods=['POST'])
def actuate():
    state = request.form['state']
    requests.post('http://actuator:5004/set', json={"state": state})
    return 'Command sent!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
