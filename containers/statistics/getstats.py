#!/usr/bin/env python

import requests
import argparse

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

def get_statistics(target, user, password):
    url = "https://" + target + "/stats"
    print("retrieve %s" % url)
    response = requests.get(url, auth=(user, password))
    print response.json


if __name__ == "__main__":
    args = parser.parse_args()
    get_statistics(args.target, args.user, args.password);


