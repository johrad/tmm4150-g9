from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

pressure = 1
battery_percentage = 0
attacks = 0


@app.route('/')
def start_page():
    data = {'pressure': pressure, 'battery_percentage': battery_percentage, 'attacks': attacks}
    return render_template('main.html', **data)


@app.route('/upload', methods=['POST'])
def receive_data():
    global pressure, battery_percentage, attacks
    data = request.get_json()

    pressure = data['pressure']
    battery_percentage = data['battery_percentage']
    attacks = data['attacks']

    return jsonify({'success': True})


@app.route('/get_data', methods=['GET'])
def get_data():
    data = {'pressure': pressure, 'battery_percentage': battery_percentage, 'attacks': attacks}
    
    return jsonify(data)    
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8044)
