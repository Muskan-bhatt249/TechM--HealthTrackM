from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Sample data (in-memory database)
patients = {}

# Route to add patient's blood report
@app.route('/api/add_report', methods=['POST'])
def add_report():
    data = request.json
    patient_id = data.get('patient_id')
    if patient_id:
        if patient_id not in patients:
            patients[patient_id] = []
        patients[patient_id].append(data)
        return jsonify({"message": "Blood report added successfully"}), 201
    else:
        return jsonify({"error": "Patient ID not provided"}), 400

# Route to get all blood reports of a patient
@app.route('/api/get_reports/<patient_id>', methods=['GET'])
def get_reports(patient_id):
    if patient_id in patients:
        return jsonify(patients[patient_id])
    else:
        return jsonify({"error": "Patient not found"}), 404

# Route to analyze blood report
@app.route('/api/analyze_report', methods=['POST'])
def analyze_report():
    data = request.json
    # Perform analysis based on blood report data
    # Example: Check if blood glucose level is high
    if data.get('blood_glucose') and float(data['blood_glucose']) > 120:
        message = "High blood glucose level detected. Please consult a doctor."
    else:
        message = "Blood report analysis complete. No issues detected."
    return jsonify({"message": message})

if __name__ == '__main__':
    app.run(debug=True)
