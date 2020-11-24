from flask import current_app as app, jsonify, make_response, request
from db.connection import db
from models.lab_details import LabDetails
from models.lab_lonic_mapping import LabLonicMapping
from models.loinc import Loinc

def get_lab_details(filters):
    filter_data = None
    if filters.get('loinc_num'):
        filter_data = filters.get('loinc_num')
    if filters.get('search'):
        filter_data = {'laboratory_name':filters.get('search')}

    details, total = LabDetails().find_all(filters.get('page',1), filters.get('limit',10), filter_data)
    return make_response(jsonify(rows=details,total=total,status='success'))

def get_lab_test_details(filters):
    filter_date = None
    if filters.get('lab_id'):
        filter_date = int(filters.get('lab_id'))
    if filters.get('search'):
        filter_date = {'component':filters.get('search')}

    lab_tests, total = Loinc().find_all(filters.get('page',1), filters.get('limit',10), filter_date)
    return make_response(jsonify(rows=lab_tests,total=total,status='success'))
