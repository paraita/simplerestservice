#!/usr/bin/env python

from flask import Flask
from flask_restplus import Resource, Api, reqparse
from werkzeug.datastructures import FileStorage
from time import sleep
from random import randint
import socket

app = Flask(__name__)
api = Api(app, version='1.0', title='LineCounter', description='This REST service exposes an endpoint that counts the lines of a given text file')

upload_parser = api.parser()
upload_parser.add_argument('text', location='files', type=FileStorage)

requests_list = []

@api.route('/lines')
@api.expect(upload_parser)
class LineCounter(Resource):
    def post(self):
        requests_list.append(1)
        args = upload_parser.parse_args()
        text = args['text']
        alloc_50MB = "a" * 50000000
        sleep(randint(2, 30))
        if text:
            result = len(text.read().decode('utf-8').split('\n'))
            requests_list.pop()
            return {'count': result}
        else:
            requests_list.pop()
            return {'count': 0}

@api.route('/info')
class ServiceName(Resource):
    def get(self):
        return {
            'service_name': 'LineCounter',
            'hostname': socket.gethostname(),
            'nb_requests': len(requests_list)
        }
    
if __name__ == '__main__':
    app.run(threaded=True, host='0.0.0.0')
