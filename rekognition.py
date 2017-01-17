#!/usr/bin/env python

import boto3
from argparse import ArgumentParser
from lib.faces import *
from lib.collections import *
from lib.labels import *
def get_client(args):
    session = boto3.Session(profile_name=args.profile_name)
    client = boto3.client('rekognition', region_name= args.region)
    return client

def get_args():
    parser = ArgumentParser(description='Call compare faces')
   # parser.add_argument('-e','--endpoint', default='https://rekognition.eu-west-1.amazonaws.com')
    parser.add_argument('-r','--region', default='eu-west-1')
    parser.add_argument('-s','--src-image')
    parser.add_argument('-t','--target-image')
    parser.add_argument('-i', '--image')
    parser.add_argument('-p','--profile_name', default='rekognition')
    parser.add_argument('-c','--collection-id')
    parser.add_argument('--face-id')
#    parser.add
    return parser.parse_args()

if __name__ == '__main__':
    args = get_args()
    client = get_client(args)
    print(compare_faces(args, client))
    print("help")
