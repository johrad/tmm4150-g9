from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

attackBoolean = 0
battery_percentage = 100
compressorBoolean = 0
attacks = 0

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
            attacks += 1
            attackBoolean = 0 # to prevent attackspam
    if 'battery_percentage' in data:
        battery_percentage = data['battery_percentage']
    if 'compressorBoolean' in data:
        compressorBoolean = data['compressorBoolean']

    print(f"Data Recieved: \n{data}\n")
    if attackBoolean:
        attacks += 1
    
    return jsonify({'success': True})

@app.route('/get_data', methods=['GET'])
def get_data():
    data = {'attackBoolean': attackBoolean, 'battery_percentage': battery_percentage, 'compressorBoolean': compressorBoolean, 'attacks': attacks}
    
    return jsonify(data)    
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8044)

