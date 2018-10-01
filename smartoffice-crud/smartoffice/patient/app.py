from flask import Blueprint
from flask import Flask, request, jsonify
import sys

# Minh's pi
# sys.path.insert(0,'/home/pi/playground/smartofficeA2/smartoffice-crud/smartoffice')
# Bram and April's pi
sys.path.insert(0,'/home/pi/A2/smartoffice-crud/smartoffice')

mod = Blueprint('patient',__name__,  template_folder='templates')

from smartoffice import model


def date_handler(obj):
    return obj.isoformat() if hasattr(obj, 'isoformat') else obj

# Add a Patient to the system
@mod.route('',methods=['POST'])
def add_patient():
    name = request.json['name']
    email = request.json['email']
    phone = request.json['phone']
    birthday = request.json['birthday']
    new_patient = model.add_patient(name, phone, birthday, email)
    return model.patient_schema.jsonify(new_patient)

# Get a Patient 
@mod.route('/<id>', methods=['GET'])
def get_patient(id):
    patient = model.get_patient(id)
    return model.patient_schema.jsonify(patient)

# Get all Patient
@mod.route('',methods=['GET'])
def get_patients():
    patients = model.get_patients()
    return model.patients_schema.jsonify(patients)

@mod.route('<id>/medical_record', methods=['GET'])
def get_patient_medical_record(id):
    records = model.get_patient_medical_record(id)
    return model.medical_records_schema.dumps(records, default = date_handler)

@mod.route('/medical_record', methods=['POST'])
def add_medical_record():
    doctor_id = request.json['doctor_id']
    patient_id = request.json['patient_id']
    date = request.json['date']
    notes = request.json['notes']
    diagnoses = request.json['diagnoses']
    record = model.add_medical_record(doctor_id, patient_id, date, notes, diagnoses)
    return model.medical_record_schema.dumps(record)
