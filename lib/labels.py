#!/usr/bin/env python


def detect_labels(args, client):
    if not args.image:
        raise Exception('Missing Image')
    with open(args.image, 'rb') as image:
        response = client.detect_labels(
                Image={
                    'Bytes': image.read()
                    },
                MaxLabels=20
                )
        return response
