from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

attackBoolean, bms_voltage, compressorState = 0,0,0

@app.route('/')
def start_page():
    data = {'attackBoolean': attackBoolean, 'bms_voltage': bms_voltage, 'compressorState': compressorState}
    return render_template('main.html', **data)

@app.route('/upload', methods=['POST'])
def receive_data():
    print("boob")
    global bms_voltage, attackBoolean, compressorState
    data = request.get_json()

    attackBoolean = data['attackBoolean']
    bms_voltage = data['bms_voltage']
    compressorState = data['compressorState']

    return jsonify({'success': True})


@app.route('/get_data', methods=['GET'])
def get_data():
    data = {'attackBoolean': attackBoolean, 'bms_voltage': bms_voltage, 'compressorState': compressorState}
    
    return jsonify(data)    
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8044)
