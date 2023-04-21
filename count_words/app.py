from flask import Flask, request
from flask_restful import Api, Resource, reqparse
from kafka import KafkaConsumer
from json import dumps, loads
#
import config as cfg


consumer = KafkaConsumer( 
    'word', 
    bootstrap_servers = cfg.KAFKA_SERVERS, 
    auto_offset_reset = 'earliest', 
    enable_auto_commit = True, 
    group_id = 'count_words', 
    value_deserializer = lambda x : loads(x.decode('utf-8')) 
) 

consumer.subscribe(['send_word'])

d = {}
while True:
    for message in consumer:
        word = message.value['word']
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
        print("-"*40)
        print(d)

#unsubscribe and close consumer
consumer.unsubscribe()
consumer.close()