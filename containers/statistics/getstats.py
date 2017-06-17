#!/usr/bin/env python

import requests
import argparse
import json
from kafka import KafkaProducer

parser = argparse.ArgumentParser(__file__, description="Fetch statistics from node")
parser.add_argument("--target",
                    "-t",
                    required=True,
                    help="Target device IP")
parser.add_argument("--user",
                    "-u",
                    required=True,
                    help="Username")
parser.add_argument("--password",
                    "-p",
                    required=True,
                    help="password")

def process_ports(value):
    ports = value['ports']
    for port in ports:
        for key, value in port.iteritems():
            print key, value


def get_statistics(target, user, password):
    url = "https://" + target + "/api/v1/nodeCounters/all"
    response = requests.get(url, auth=(user, password), verify=False)
    payload = response.json()
    for key, value in payload.iteritems():
	#print key, value
        if (key == 'ports'):
            process_ports(value)


if __name__ == "__main__":
    producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda v:json.dumps(v).encode('utf-8'))
    args = parser.parse_args()
    requests.packages.urllib3.disable_warnings()
    get_statistics(args.target, args.user, args.password);



