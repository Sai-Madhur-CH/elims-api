from flask import current_app as app, jsonify, request, make_response
from flask_restful import Resource
import services.lab_catalog_service as lcs


class LabList(Resource):
    """
    To get all the lab details
    """
    def get(self):
        filters = request.args.to_dict()
        return lcs.get_lab_details(filters)


class LabTestList(Resource):
    """
    To get all the lab test details
    """
    def get(self):
        filters = request.args.to_dict()
        return lcs.get_lab_test_details(filters)
