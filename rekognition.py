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


def execute_actions(args, client):
    if not args.action:
        raise Exception("No action defined")
    else:
        actions = {
                "detect-labels": labels.detect_labels,
                "detect-faces": faces.detect_faces,
                "compare-faces": faces.compare_faces,
                "index-faces": faces.index_faces,
                "search-faces": faces.search_faces,
                "search-faces-by-image": faces.search_faces_by_image,
                "delete-faces": faces.delete_faces,
                "list-faces": faces.list_faces,
                "create-collection": collections.create_collection,
                "delete-collection": collections.delete_collection,
                "list-collections": collections.list_collections
                }
        if args.action not in actions:
            raise Exception("No such action")
        else:
            return (actions.get(args.action)(args, client))


if __name__ == '__main__':
    args = get_args()
    client = get_client(args)
    if args.action:
        print(execute_actions(args, client))
    print("help")
