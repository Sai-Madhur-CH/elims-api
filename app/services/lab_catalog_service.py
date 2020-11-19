from flask import current_app as app, jsonify, make_response, request
from db.connection import db
from models.lab_details import LabDetails
from models.lab_lonic_mapping import LabLonicMapping
from models.loinc import Loinc

def get_lab_details(filters):
    fliter_data = None
    if filters.get('loinc_num'):
        fliter_data = filters.get('loinc_num')
    details, total = LabDetails().find_all(filters.get('page',1), filters.get('limit',10), fliter_data)
    return make_response(jsonify(rows=details,total=total,status='success'))

def get_lab_test_details(filters):
    fliter_data = dict()
    if filters.get('lab_id'):
        fliter_data = int(filters.get('lab_id'))
    lab_tests, total = Loinc().find_all(filters.get('page',1), filters.get('limit',10), fliter_data)
    return make_response(jsonify(rows=lab_tests,total=total,status='success'))
