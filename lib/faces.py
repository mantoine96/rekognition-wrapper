#!/usr/bin/env python


def detect_faces(args, client):
    if not args.image:
        raise Exception('Missing Image')
    with open(args.image, 'rb') as image:
        response = client.detect_faces(
                Image={
                    'Bytes': image.read()
                    },
                MaxLabels=20,
                Attributes=[
                    'ALL'
                    ]
                )
        return response


def compare_faces(args, client):
    if not args.src_image:
        raise Exception('Missing Source Image')
    if not args.target_image:
        raise Exception('Missing Target Image')
    with open(args.src_image, 'rb') as src_image:
        with open(args.target_image, 'rb') as target_image:
            response = client.compare_faces(
                    SourceImage={
                        'Bytes': src_image.read(),
                        },
                    TargetImage={
                        'Bytes': target_image.read(),
                        },
                    SimilarityThreshold=50
                    )
            return response


def index_faces(args, client):
    if not args.image:
        raise Exception("Missing Image")
    if not args.collection_id:
        raise Exception("Missing Collection ID")
    with open(args.image, 'rb') as image:
        response = client.index_faces(
                CollectionId=args.collection_id,
                Image={
                    'Bytes': image.read()
                    },
                DetectionAttributes=[
                    'ALL'
                    ]
                )
        return response


def search_faces(args, client):
    if not args.image:
        raise Exception("Missing Image")
    if not args.collection_id:
        raise Exception("Missing Collection ID")
    if not args.face_id:
        raise Exception("Missing Face ID")
    with open(args.image, 'rb') as image:
        response = client.search_faces(
                SourceImage={
                    'Bytes': image.read()
                    },
                CollectionId=str(args.collection_id),
                FaceId=str(args.face_id)
                )
        return response


def search_faces_by_image(args, client):
    if not args.image:
        raise Exception("Missing Image")
    if not args.collection_id:
        raise Exception("Missing Collection ID")
    with open(args.image, 'rb') as image:
        response = client.search_faces_by_image(
                CollectionId=str(args.collection_id),
                Image={
                    'Bytes': image.read()
                    }
                )
        return response


def delete_faces(args, client):
    if not args.face_ids:
        raise Exception("Missing Face IDs")
    if not args.collection_id:
        raise Exception("Missing Collection ID")
    face_ids = []
    for face_id in args.face_ids:
        face_ids.append(face_id)
    response = client.delete_faces(
            CollectionId=args.collection_id,
            FaceIds=face_ids
            )
    return response


def list_faces(args, client):
    if not args.collection_id:
        raise Exception("Missing Collection ID")
    response = client.list_faces(
            CollectionId=str(args.collection_id)
            )
    return response
