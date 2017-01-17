#!/usr/bin/env python

import boto3
from argparse import ArgumentParser
from lib import faces, collections, labels


def get_client(args):
    boto3.Session(profile_name=args.profile_name)
    client = boto3.client('rekognition', region_name=args.region)
    return client


def get_args():
    parser = ArgumentParser(description='Call compare faces')
    parser.add_argument('-r', '--region', default='eu-west-1')
    parser.add_argument('-s', '--src-image')
    parser.add_argument('-t', '--target-image')
    parser.add_argument('-i',  '--image')
    parser.add_argument('-p', '--profile_name', default='rekognition')
    parser.add_argument('-c', '--collection-id')
    parser.add_argument('--face-id')
    parser.add_argument('action', metavar='ACTION', type=str,
                        help='which action to execute')
    # parser.add
    return parser.parse_args()

dict available_actions = {

        }

if __name__ == '__main__':
    args = get_args()
    client = get_client(args)
    print(args.action)
    print(faces.compare_faces(args, client))
    print("help")
