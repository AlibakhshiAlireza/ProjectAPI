from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory database
database = {
    "1": 25,
    "2": 15,
    "3": 15,
    "4": 20,
    "5": 30,
    "6": 9,
    "7": 8
}

@app.route('/slots', methods=['GET'])
def get_slots():
    return jsonify(database)

@app.route('/reserve', methods=['POST'])
def reserve_slot():
    data = request.json
    clinic_id = str(data.get('id'))
    reserved = data.get('reserved', 0)

    if clinic_id in database and database[clinic_id] >= reserved:
        database[clinic_id] -= reserved
        return jsonify({"success": True, "remaining_slots": database[clinic_id]})
    else:
        return jsonify({"success": False, "message": "Invalid request"}), 400

if __name__ == '__main__':
    app.run(debug=True)
