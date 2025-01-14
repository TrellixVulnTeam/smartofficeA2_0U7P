from flask import Blueprint
from flask import Flask, render_template, session, url_for, redirect, request
import time
import sys

# Minh's pi
# sys.path.insert(0,'/home/pi/playground/smartofficeA2/smartoffice-crud/smartoffice')
# Bram and April's pi
sys.path.insert(0,'/home/pi/A2/smartoffice-crud/smartoffice')

mod = Blueprint('doctor',__name__, template_folder='templates')

from smartoffice import model

# Add a Doctor to the system
@mod.route('',methods=['POST'])
def add_doctor():
    """Add doctor API"""
    name = request.json['name']
    email = request.json['email']
    major = request.json['major']
    calendar_id = model.add_calendar(name)
    new_doctor = model.add_doctor(name, email, major, calendar_id)
    return model.doctor_schema.jsonify(new_doctor)

# Get All Doctor
@mod.route('',methods=['GET'])
def get_doctors():
    """Get all doctors API"""
    doctors = model.get_doctors()
    return model.doctors_schema.jsonify(doctors)

# Get Doctor by Id
@mod.route('/<id>', methods=['GET'])
def get_doctor(id):
    """Get doctor by ID API"""
    doctor = model.get_doctor(id)
    return model.doctor_schema.jsonify(doctor)

@mod.route('/name/<name>', methods=['GET'])
def get_doctor_by_name(name):
    """Get doctor by name API"""
    doctor = model.get_doctor_by_name(name)
    return model.doctor_schema.jsonify(doctor)