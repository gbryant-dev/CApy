import requests
from requests import Response
from typing import List, Optional, Tuple
import json

http_client = requests.session()
_headers = {
  "Content-Type": "application/json"
}
BASE_URL = '{BASE_URL}'
XSRF_COOKIE = 'XSRF-TOKEN'
XSRF_HEADER = 'X-XSRF-TOKEN'


def main():
    
    if not _headers.get(XSRF_HEADER):
        token = get_xsrf_token()
        _headers[XSRF_HEADER] = token

    # Need to pass username, password and namespace (optional)
    login('username', 'password', '[namespace]')

    # Do whatever we want

def login(username: str, password: str, namespace: Optional[str] = None) -> Response:

    """
        :param username: str,
        :param password: str,
        :param namespace: str, Optional
    """

    payload = dict()
    payload['parameters'] = [
    {
        "name": "CAMUsername",
        "value": username
    },
    {
        "name": "CAMPassword",
        "value": password
    }
    ]

    if namespace:
        payload['parameters'].append({ "name": "CAMNamespace", "value": namespace })

    return http_client.put(BASE_URL + '/api/v1/session', data=json.dumps(payload), headers=_headers)
    

def get_xsrf_token() -> str:
    url = '/api/v1/session'
    response = http_client.get(BASE_URL + url)
    token = response.cookies.get(XSRF_COOKIE, None)
    if not token:
        raise RuntimeError('Could not extract XSRF token from headers')
    return token


def get_group(id: str) -> Response:
    url = "/api/v1/groups/{}".format(id)
    response = http_client.get(BASE_URL + url, headers=_headers)
    return response.json()

def get_groups(parent_id: Optional[str] = None) -> List:
    url = "/api/v1/groups{parent_id}".format(parent_id=f"?parent_id={parent_id}" if parent_id else "")
    response = http_client.get(BASE_URL + url, headers=_headers)
    return [group for group in response.json()['groups']]

def get_group_members(id: str) -> Tuple[List, List]:
    url = "/api/v1/groups/{}/members".format(id)
    json = http_client.get(BASE_URL + url, headers=_headers).json()
    users, groups = json['users'], json['groups']
    return users, groups

def add_member_to_group(group_id: str, user_ids: List[str] = None, group_ids: List[str] = None) -> Response:
    url = "/api/v1/groups/{}/members".format(group_id)
    payload = dict()
    if not user_ids and not group_ids:
        raise ValueError('Must provide at least user_ids or group_ids')

    if user_ids:
        users = [{ "id": user_id} for user_id in user_ids]
        payload['users'] = users
    
    if group_ids:
        groups = [{ "id": group_id } for group_id in group_ids]
        payload['groups'] = groups  

    print(payload)  

    return http_client.post(BASE_URL + url, data=json.dumps(payload), headers=_headers)

def delete_member_from_group(group_id: str, member_type: str, member_id: str) -> Response:
    url = "/api/v1/groups/{}/members/{}/{}".format(group_id, member_type, member_id)
    return http_client.delete(BASE_URL + url, headers=_headers)

def get_user(id: str) -> Response:
    url = "/api/v1/users/{}".format(id)
    response = http_client.get(BASE_URL + url, headers=_headers)
    return response.json()

def get_users(id: str) -> Response:
    url = "/api/v1/users?identifier={}".format(id)
    response = http_client.get(BASE_URL + url, headers=_headers)
    return [user for user in response.json()['users']]

if __name__ == '__main__':
    main()