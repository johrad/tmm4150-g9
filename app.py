from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

attackBoolean = 0
battery_percentage = 100
compressorBoolean = 0

attacks = 0
attacksOld = 0

# min_voltage = 11.7
# max_voltage = 12.6
# voltage_range = max_voltage - min_voltage

# def voltage_to_percentage(current_voltage):
#     voltage_offset = current_voltage - min_voltage
#     percentage = (voltage_offset / voltage_range) * 100
#     percentage = max(0, min(100, percentage))
    
#     return percentage

@app.route('/')
def start_page():
    data = {'battery_percentage': battery_percentage, 'attacks': attacks}
    return render_template('main.html', **data)

@app.route('/upload', methods=['POST'])
def receive_data():
    global attackBoolean, battery_percentage, compressorBoolean, attacks
    data = request.get_json()

    # Update only the received values if present
    if 'attackBoolean' in data:
        attackBoolean = data['attackBoolean']
        if attackBoolean == 1:
            attacks += 1  # to prevent attackspam
            attackBoolean = 0
    if 'battery_percentage' in data:
        battery_percentage = data['battery_percentage']
    if 'compressorBoolean' in data:
        compressorBoolean = data['compressorBoolean']

    print(f"Data Recieved: \n{data}\n")

    return jsonify({'success': True})

@app.route('/get_data', methods=['GET'])
def get_data():
    data = {'attackBoolean': attackBoolean, 'battery_percentage': battery_percentage, 'compressorBoolean': compressorBoolean, 'attacks': attacks}
    
    return jsonify(data)    
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8044)

