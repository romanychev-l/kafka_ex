import random
import numpy
import requests
#
from datetime import datetime
from flask import Flask, request
from flask_restful import Api, Resource, reqparse
from kafka import KafkaProducer
from json import dumps 
#
import config as cfg


def main(word):
    data = {'word' : word } 
    producer.send('send_word', value = data)
    return "Success"


app = Flask(__name__)
api = Api(app)

producer = KafkaProducer( 
    bootstrap_servers = cfg.KAFKA_SERVERS, 
    value_serializer = lambda x: dumps(x).encode('utf-8') 
)

class GetInt(Resource):
    def get(self, word=0):
        ans = main(word)
        return ans, 200
    
api.add_resource(GetInt, "/api/v1/push", "/api/v1/push/", "/api/v1/push/<string:word>")

if __name__ == '__main__':
    app.run(debug=True)
    producer.close()