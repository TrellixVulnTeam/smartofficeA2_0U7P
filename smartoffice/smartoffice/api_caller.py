"""This module contain functions that make request to API"""

import requests
import json
from datetime import datetime
import sys

sys.path.insert(0,'/home/pi/A2/smartoffice/smartoffice/config/')
import api_config

class Patient():
    """Patient Class""" 
    def __init__(self, id, name, phone, birthday, email):
        """Patient Initializer"""
        self.id = id
        self.name = name
        self.phone = phone
        self.birthday = birthday
        self.email = email

class Doctor():
    """Doctor Class"""
    def __init__(self, id, name, email, major, calendar_id):
        """Doctor Initializer"""
        self.id = id
        self.name = name
        self.major = major
        self.email = email
        self.calendar_id = calendar_id

class Clerk():
    """Clerk Class"""
    def __init__(self, id, name, email):
        """Clerk Initializer"""
        self.id = id
        self.name = name
        self.email = email
    
class Appointment():
    """Appointment Class"""
    def __init__(self, id, doctor_id, date, time_start, time_end, patient_id, event_id):
        """Appointment Initializer"""
        self.id = id
        self.doctor_id = doctor_id
        self.date = date
        self.time_start = time_start
        self.time_end = time_end
        self.patient_id = patient_id
        self.event_id = event_id

class Availability():
    """Availability Class"""
    def __init__(self, id, doctor_id, date, time_start, time_end, event_id):
        """Availability Initializer"""
        self.id = id
        self.doctor_id = doctor_id
        self.date = date
        self.time_start = time_start
        self.time_end = time_end
        self.event_id = event_id

class MedicalRecord():
    """Medical Record Class"""
    def __init__(self, id, doctor_id, patient_id, date, notes):
        """Medical Record Initializer"""
        self.id = id
        self.doctor_id = doctor_id
        self.patient_id = patient_id
        self.date = date
        self.notes = notes

URL = api_config.get_api_domain()
patient_code = 'patient'
doctor_code = 'doctor'
clerk_code = 'clerk'
appointment_code = 'appointment'
availability_code = 'availability'
calendar_code = 'calendar'


# Patient API caller
def get_patient(id):
    """Get Patient by Id"""
    url = URL + patient_code + "/"+ str(id)
    try:
        response = requests.get(url)
        json_data = response.json()
        patient = Patient(json_data['id'], json_data['name'], json_data['phone'], json_data['birthday'], json_data['email'])
        print("Patient retrieve")
        return patient
    except:
        print("Error Occur")
        return None

# add patient to the system
def add_patient(name, phone, birthday, email):
    """Add Patient"""
    url = URL + patient_code
    data_send = {
        "name": name,
        "phone": phone,
        "birthday": birthday,
        "email": email
    }
    try:
        response = requests.post(url, 
            data = json.dumps(data_send),
            headers = {'Content-Type':'application/json'}
        )
        print("Patient added to the system")
        return True
    except:
        print("Unable to add patient, Error Occur")
        return False

# get all the patients
def get_patients():
    """Get All Patients"""
    url = URL + patient_code
    patients = []
    try:
        response = requests.get(url)
        json_data = response.json()
        for patient_json in json_data:
            patient = Patient(patient_json['id'], patient_json['name'], patient_json['phone'], patient_json['birthday'], patient_json['email'])
            patients.append(patient)
        print("Patients retrieved")
        return patients
    except:
        print("Unable to get patients, Error Occur")
        return None

# Doctor API caller
    # get all the doctor
def get_doctors():
    """Get All Doctors"""
    url = URL + doctor_code
    doctors = []
    try: 
        response = requests.get(url)
        json_data = response.json()
        for doctor_json in json_data:
            doctor = Doctor(doctor_json['id'], doctor_json['name'], doctor_json['email'], doctor_json['major'], doctor_json['calendar_id'])
            doctors.append(doctor)
        return doctors
        print("Doctors Retrieved")
    except:
        print("Unable to get doctors, Error Occur")
        return None

    # add doctor to the system
def add_doctor( name, major, email, calendar_id):
    """Add Doctor"""
    url = URL + doctor_code
    data_send = {
        "name": name,
        "major":major,
        "email": email,
        "calendar_id":None
    }
    try:
        response = requests.post(url, 
            data = json.dumps(data_send),
            headers = {'Content-Type':'application/json'}
        )
        print("Doctor added to the system")
        return True
    except:
        print("Unable to add doctor, Error Occur")
        return False

def get_doctor(id):
    """Get Doctor by ID"""
    url = URL + doctor_code + "/"+ str(id)
    doctors = []
    try:
        response = requests.get(url)
        json_data = response.json()
        doctor = Doctor(json_data['id'], json_data['name'], json_data['email'], json_data['major'], json_data['calendar_id'])
        return doctor
        print("Doctor retrieve")
    except:
        print("Error Occur")
        return None

# get all the clerks
def get_clerks():
    """Get All Clerks"""
    url = URL + clerk_code
    clerks = []
    try:
        response = requests.get(url)
        json_data = response.json()
        for clerk_json in json_data:
            clerk = Clerk(clerk_json['id'], clerk_json['name'], clerk_json['email'])
            clerks.append(clerk)
        print("Clerks retrieved")
        return clerks
    except:
        print("Unable to get clerks, Error Occur")
        return None

# add clerk to the system
def add_clerk(name, email):
    """Add Clerk"""
    url = URL + clerk_code
    data_send = {
        "name": name,
        "email": email,
    }
    try:
        response = requests.post(url, 
            data = json.dumps(data_send),
            headers = {'Content-Type':'application/json'}
        )
        print("Clerk added to the system")
        return True
    except:
        print("Unable to add clerk, Error Occur")
        return False


def get_clerk(id):
    """Get Clerk by ID"""
    url = URL + clerk_code + "/"+ str(id)
    try:
        response = requests.get(url)
        json_data = response.json()
        clerk = Clerk(json_data['id'], json_data['name'], json_data['email'])
        print("Clerk retrieve")
        return clerk
    except:
        print("Error Occur")
        return None

# Appointment API Caller
# add a appointment
def add_appointment(doctor_id, date, time_start, time_end, patient_id, event_id):
    """Add Appointment"""
    url = URL + appointment_code
    data_send = {
        "doctor_id": doctor_id,
        "date": date,
        "time_start": time_start,
        "time_end": time_end,
        "patient_id": patient_id,
        "event_id": event_id
    }
    try:
        response = requests.post(url,
            data = json.dumps(data_send),
            headers = {'Content-Type':'application/json'}
        )
        print("Appointment have been added")
        return True
    except:
        print("Unable to add Appointment, Error Occur")
        return False

    # Get All Appointments
def get_appointments():
    """Get All Appointments"""
    url = URL + appointment_code
    appointments = []
    try:
        response = requests.get(url)
        json_data = response.json()
        for appointment_json in json_data:
            appointment = Appointment(appointment_json['id'],
                appointment_json['doctor_id'], appointment_json['date'], 
                appointment_json['time_start'], appointment_json['time_end'], 
                appointment_json['patient_id'], appointment_json['event_id']
                )
            appointments.append(appointment)
        print("Retrieve Appointments")
        return appointments
    except:
        print("Unable to get Appointments, Error Occur")
        return None

    # Get Appointment by Id        
def get_appointment(id):
    """Get Appointment by ID"""
    url = URL + appointment_code + "/"+ str(id)
    try:
        response = requests.get(url)
        json_data = response.json()
        appointment = Appointment(json_data['id'],
            json_data['doctor_id'], json_data['date'], 
            json_data['time_start'], json_data['time_end'], 
            json_data['patient_id'], json_data['event_id']
            )
        print("Retrieve Appointment")
        return appointment
    except:
        print("Unable to get Appointment, Error Occur")
        return None

def remove_appointment(id):
    """Remove Appointment by ID"""
    url = URL + appointment_code + "/" + str(id)
    try:
        response = requests.delete(url)
        return True
    except:
        print("Cannot delete appointment, Error Occur")
        return False

def get_available_appointments():
    """Get All available appointments"""
    url = URL + appointment_code + "/available"
    appointments = []
    try:
        response = requests.get(url)
        json_data = response.json()
        for appointment_json in json_data:
            appointment = Appointment(appointment_json['id'],
                appointment_json['doctor_id'], appointment_json['date'], 
                appointment_json['time_start'], appointment_json['time_end'], 
                appointment_json['patient_id'], appointment_json['event_id']
                )
            appointments.append(appointment)
        print("Retrieve Appointments")
        return appointments
    except:
        print("Unable to get Appointments, Error Occur")
        return None

def get_available_appointments_by_doctor(id):
    """Get available appointments by doctor ID"""
    url = URL + appointment_code + "/available/doctor/" + str(id)
    appointments = []
    try:
        response = requests.get(url)
        json_data = response.json()
        for appointment_json in json_data:
            appointment = Appointment(appointment_json['id'],
                appointment_json['doctor_id'], appointment_json['date'], 
                appointment_json['time_start'], appointment_json['time_end'], 
                appointment_json['patient_id'], appointment_json['event_id']
                )
            appointments.append(appointment)
        print("Retrieve Appointments")
        return appointments
    except:
        print("Unable to get Appointments, Error Occur")
        return None

def get_available_appointments_by_patient(id):
    url = URL + appointment_code + "/available/patient/" + str(id)
    appointments = []
    try:
        response = requests.get(url)
        json_data = response.json()
        for appointment_json in json_data:
            appointment = Appointment(appointment_json['id'],
                appointment_json['patient_id'], appointment_json['date'], 
                appointment_json['time_start'], appointment_json['time_end'], 
                appointment_json['doctor_id'], appointment_json['event_id']
                )
            appointments.append(appointment)
        print("Retrieve Appointments")
        return appointments
    except:
        print("Unable to get Appointments, Error Occur")
        return None

def get_appointments_by_patient(id):
    """Get appointment by Patient ID"""
    url = URL + appointment_code + "/patient/" + str(id)
    appointments = []
    try:
        response = requests.get(url)
        json_data = response.json()
        for appointment_json in json_data:
            appointment = Appointment(appointment_json['id'],
                appointment_json['doctor_id'], appointment_json['date'], 
                appointment_json['time_start'], appointment_json['time_end'], 
                appointment_json['patient_id'], appointment_json['event_id']
                )
            appointments.append(appointment)
        print("Retrieve Appointments")
        return appointments
    except:
        print("Unable to get Appointments, Error Occur")
        return None

def get_appointments_by_doctor(id):
    """Get appointments by doctor ID"""
    url = URL + appointment_code + "/doctor/" + str(id)
    appointments = []
    try:
        response = requests.get(url)
        json_data = response.json()
        for appointment_json in json_data:
            appointment = Appointment(appointment_json['id'],
                appointment_json['doctor_id'], appointment_json['date'], 
                appointment_json['time_start'], appointment_json['time_end'], 
                appointment_json['patient_id'], appointment_json['event_id']
                )
            appointments.append(appointment)
        print("Retrieve Appointments")
        return appointments
    except:
        print("Unable to get Appointments, Error Occur")
        return None

def get_appointments_by_doctor_and_date(doctor_id, input_date):
    """Get available appointments by doctor ID and Date"""
    url = URL + appointment_code + "/doctor/bydate" 
    data_send = {
        "doctor_id": doctor_id,
        "input_date": input_date
    }
    appointments = []
    try:
        response = requests.post(url,
            data = json.dumps(data_send),
            headers = {'Content-Type':'application/json'}
            )
        json_data = response.json()
        for appointment_json in json_data:
            appointment = Appointment(appointment_json['id'],
                appointment_json['doctor_id'], appointment_json['date'], 
                appointment_json['time_start'], appointment_json['time_end'], 
                appointment_json['patient_id'], appointment_json['event_id']
                )
            appointments.append(appointment)
        print("Retrieve Appointments")
        return appointments
    except:
        print("Unable to get Appointments, Error Occur")
        return None        

def get_upcoming_appointments_by_doctor(id):
    """Get upcoming appointments by doctor ID"""
    url = URL + appointment_code + "/doctor/next/" + str(id)
    appointments = []
    try:
        response = requests.get(url)
        json_data = response.json()
        for appointment_json in json_data:
            appointment = Appointment(appointment_json['id'],
                appointment_json['doctor_id'], appointment_json['date'], 
                appointment_json['time_start'], appointment_json['time_end'], 
                appointment_json['patient_id'], appointment_json['event_id']
                )
            appointments.append(appointment)
        print("Retrieve Appointments")
        return appointments
    except:
        print("Unable to get Appointments, Error Occur")
        return None

def book_appointment(appointment_id, patient_id):
    """Book appointment"""
    url = URL + appointment_code + "/book"
    data_send = {
        "appointment_id": appointment_id,
        "patient_id": patient_id
    }
    try:
        response = requests.put(url,
            data = json.dumps(data_send),
            headers = {'Content-Type':'application/json'}
        )
        print("Appointment Booked")
        return True
    except:
        print("Unable to Book the appointment, Error Occur")
        return False

def unbook_appointment(appointment_id):
    """Unbook appointment"""
    url = URL + appointment_code + "/unbook"
    data_send = {
        "appointment_id": appointment_id
    }
    try:
        response = requests.put(url,
            data = json.dumps(data_send),
            headers = {'Content-Type':'application/json'}
        )
        print("Appointment Unbooked")
        return True
    except:
        print("Unable to Unbook the appointment, Error Occur")
        return False



# Availability API Caller
def add_availability(doctor_id, date, time_start, time_end, event_id):
    """Add availability"""
    url = URL + availability_code
    data_send = {
        "doctor_id": doctor_id,
        "date": date,
        "time_start": time_start,
        "time_end": time_end,
        "event_id": event_id
    }
    try:
        response = requests.post(url,
            data = json.dumps(data_send),
            headers = {'Content-Type':'application/json'}
            )
        print("Availability Added to the system")
        return True
    except:
        print("Unable to add Availability to the system, Error Occur")
        return False

def get_availability():
    """Get availability"""
    url = URL + availability_code
    availabilities = []
    try:
        response = requests.get(url)
        json_data = response.json()
        for avail_json in json_data:
            availability = Availability(avail_json['id'], avail_json['doctor_id'],
                avail_json['date'], avail_json['time_start'], avail_json['time_end'],
                avail_json['event_id']
                )
            availabilities.append(availability)
        print("Retrieve Availabilities")
        return availabilities
    except:
        print("Unable to retrieve availabilities, Error Occur")
        return None

def get_availability_by_doctor(id):
    """Get availability by doctor ID"""
    url = URL + availability_code + "/doctor/" + str(id)
    availabilities = []
    try:
        response = requests.get(url)
        json_data = response.json()
        for avail_json in json_data:
            availability = Availability(avail_json['id'], avail_json['doctor_id'],
                avail_json['date'], avail_json['time_start'], avail_json['time_end'],
                avail_json['event_id']
                )
            availabilities.append(availability)
        print("Retrieve Availabilities")
        return availabilities
    except:
        print("Unable to retrieve availabilities, Error Occur")
        return None

def remove_availability(id):
    """Remove availability by ID"""
    url = URL + availability_code + "/" + str(id)
    try: 
        response = requests.delete(url)
        print("Remove Availability")
        return True
    except:
        print("Unable to remove availability, Error Occur")
        return False

# Calendar API Caller

def remove_from_calendar(calendar_id, event_id):
    """Remove event from calendar"""
    url = URL + calendar_code
    data_send = {
        "calendar_id": calendar_id,
        "event_id": event_id
    }
    try:
        response = requests.delete(url,
            data = json.dumps(data_send),
            headers = {'Content-Type':'application/json'}
            )
        print("Remove Event")
        return True
    except:
        print("Unable to remove event, Error Occur")
        return False

def add_to_calendar(summary, doctor_id, date, time_start, time_end, calendar_id):
    """Add event from calendar"""
    url = URL + calendar_code
    data_send = {
        "summary": summary,
        "doctor_id": doctor_id,
        "date": date,
        "time_start": time_start,
        "time_end": time_end,
        "calendar_id": calendar_id
    }
    try:
        response = requests.post(url,
            data = json.dumps(data_send),
            headers = {'Content-Type':'application/json'}
            )
        event_id = response.json()
        return event_id
    except:
        print("Unable to add event into the Calendar, Error Occur")
        return ""

def get_patient_medical_record(id):
    """Get Patient medical records"""
    url = URL + patient_code +"/" + str(id) + "/medical_record"
    # url = URL + patient_code + "/medical_record" + str(id)
    records = []
    try:
        response = requests.get(url)
        json_data = response.json()
        for record_json in json_data:
            record = MedicalRecord(record_json['id'], record_json['doctor_id'], 
                record_json['patient_id'], record_json['date'], record_json['notes'])
            records.append(record)
        return records
    except:
        return None

def add_medical_record(doctor_id, patient_id, notes):
    """Add medical record for a patient"""
    url = URL + patient_code + "/medical_record"
    date = datetime.now()
    date = datetime.strftime(date, "%Y-%m-%d")
    data_send = {
        "doctor_id": doctor_id,
        "patient_id": patient_id,
        "date": date,
        "notes":notes
    }
    try: 
        response = requests.post(url,
            data = json.dumps(data_send),
            headers = {'Content-Type':'application/json'}
            )
        print("Record Added")
        return True
    except:
        print("Error Occur")
        return False

def get_patient_by_name(name):
    """Get Patient by name"""
    url = URL + patient_code + "/name/" + str(name)
    try:
        response = requests.get(url)
        json_data = response.json()
        patient = Patient(json_data['id'], json_data['name'], json_data['phone'], json_data['birthday'], json_data['email'])
        return patient
    except:
        return None

def get_doctor_by_name(name):
    """Get Doctor by name"""
    url = URL + doctor_code + "/name/" + str(name)
    try:
        response = requests.get(url)
        json_data = response.json()
        doctor = Doctor(json_data['id'], json_data['name'], json_data['email'], json_data['major'], json_data['calendar_id'])
        return doctor
    except:
        return None
