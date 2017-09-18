#!/usr/bin/env python

from flask import Flask
from flask_restplus import Resource, Api, reqparse
from werkzeug.datastructures import FileStorage
import socket
import psutil

app = Flask(__name__)
api = Api(app, version='1.0', title='WordCounter', description='This REST service exposes an endpoint that counts the words of a given text file')

upload_parser = api.parser()
upload_parser.add_argument('text', location='files', type=FileStorage)

@api.route('/words')
@api.expect(upload_parser)
class WordCounter(Resource):
    def post(self):
        args = upload_parser.parse_args()
        text = args['text']
        if text:
            result = len(text.read().decode('utf-8').split())
            return {'count': result}
        else:
            return {'count': 0}

@api.route('/info')
class ServiceName(Resource):
    def get(self):
        return {
            'service_name': 'WordCounter',
            'hostname': socket.gethostname(),
            'cpu_load': psutil.cpu_percent()
        }
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
