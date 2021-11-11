import requests
import json


def get_streams(fs_server_ip='127.0.0.1', fs_server_port='34569'):
    url = api_methods['streams'].format('http://' + fs_server_ip + ':' + fs_server_port)
    headers = {
        'Content-Type': 'application/json'
    }

    try:
        response = requests.get(url, headers=headers)
        body = json.loads(response.content)

        return body
    except (requests.ConnectionError, KeyError):
        return False

#cleanup_streams('10.10.220.211') get_streams('10.10.220.211')
def cleanup_streams(fs_server_ip='127.0.0.1', fs_server_port='34569'):
    url = api_methods['streams'].format('http://' + fs_server_ip + ':' + fs_server_port)
    headers = {
        'Content-Type': 'application/json'
    }
    stream_array = list()
    for id in get_streams(fs_server_ip, fs_server_port):
        stream_array.append(id['id'])

    try:
        response = requests.delete(url, headers=headers, json=stream_array)
        body = json.loads(response.content)

        return body
    except:
        return False


def add_basic_stream(fs_server_ip='127.0.0.1', fs_server_port='34569',
                     stream_url='rtsp://127.0.0.1:554/Streaming/Channels/1',
                     luna_url='http://127.0.0.1:5000/6/handlers/deadbeef-0000-1111-2222-deadbeef0000/events',
                     luna_aid='deadbeef-0000-1111-2222-deadbeef0000'):
    url = api_methods['streams'].format('http://' + fs_server_ip + ':' + fs_server_port)
    headers = {
        'Content-Type': 'application/json'
    }

    data = [
        {
            "name": "stream_0",
            "input": {
                "url": stream_url,
            },
            "output": {
                "luna-account-id": luna_aid,
                "url": luna_url,
            }
        }
    ]

    try:
        response = requests.get(url, headers=headers)
        body = json.loads(response.content)

        return body
    except (requests.ConnectionError, KeyError):
        return False


api_methods = {
    'streams': '{0}/api/1/streams',
}
