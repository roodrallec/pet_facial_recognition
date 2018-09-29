import argparse
import json
import os


def response(status, message):
    return {
        'statusCode': status,
        'body': message
    }


def train():
    return train_faces()


def identify(event={}, context={}):
    print('New event', event)

    try:
        params = event['queryStringParameters'] or {}

        if params['access_token'] != os.environ['ACCESS_TOKEN']:
            return response(400, 'Invalid access token')

        return response(400, 'Invalid path ' + str(event['path']))

    except KeyError as e:
        return response(400, 'Missing query parameters ' + str(e))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--image_url', default='https://images.pexels.com/photos/358464/pexels-photo-358464.jpeg?auto=compress&cs=tinysrgb&h=350')
    args = parser.parse_args()

    print(identify({'image_url': args.image_url, 'access_token': os.environ['ACCESS_TOKEN']}))
