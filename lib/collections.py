#!/usr/bin/env python


def create_collection(args, client):
    if not args.collection_id:
        raise Exception("Missing Collection ID")
    response = client.create_collection(
            CollectionId=str(args.collection_id)
            )
    return response


def delete_collection(args, client):
    if not args.collection_id:
        raise Exception("Missing Collection ID")
    response = client.delete_collection(
            CollectionId=str(args.collection_id)
            )
    return response


def list_collections(args, client):
    response = client.list_collections()
    return response
