from flask_restful import Resource
from flask import request
import json
import xml.etree.ElementTree as ET

def to_xml(data):
    if isinstance(data, list):
        root = ET.Element('data')
        for item in data:
            element = ET.SubElement(root, 'item')
            for key, value in item.items():
                child = ET.SubElement(element, key)
                child.text = str(value)
    else:
        root = ET.Element('driver')
        for key, value in data.items():
            child = ET.SubElement(root, key)
            child.text = str(value)
    return ET.tostring(root, encoding='utf-8', method='xml')

class ReportResource(Resource):
    def __init__(self, **kwargs):
        self.report_generator = kwargs['report_generator']

    def get(self):
        format_type = request.args.get('format', 'json')
        order = request.args.get('order', 'asc')
        report_data = self.report_generator.get_report_data(order)
        if format_type == 'xml':
            return to_xml(report_data)
        return report_data

class DriversResource(Resource):
    def __init__(self, **kwargs):
        self.report_generator = kwargs['report_generator']

    def get(self):
        format_type = request.args.get('format', 'json')
        drivers_data = self.report_generator.get_all_drivers()
        if format_type == 'xml':
            return to_xml(drivers_data)
        return drivers_data

class DriverInfoResource(Resource):
    def __init__(self, **kwargs):
        self.report_generator = kwargs['report_generator']

    def get(self, driver_id):
        format_type = request.args.get('format', 'json')
        driver_info = self.report_generator.get_driver_info(driver_id)
        if format_type == 'xml':
            return to_xml(driver_info)
        return driver_info