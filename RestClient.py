import json
from typing import Dict, Union, Optional
import requests

class RestClient:

    XSRF_COOKIE = 'XSRF-Token'
    XSRF_HEADER = 'X-XSRF-Token'

    def __init__(
        self, 
        address: str, 
        user: str, 
        password: str, 
        port: int, 
        ssl: bool, 
        namespace: Optional[str] = None
    ):

        self._base_url = "http{}//{}:{}".format(
            's' if ssl else '', 
            'localhost' if len(address) == 0 else address,
            port)
        self._headers = dict()
        self._http = requests.session()
        self._verify = False

        self._start_session(user, password, namespace)


    def _start_session(self, user: str, password: str, namespace: str = None):
        url = '/api/v1/session'
        if not self._headers.get(self.XSRF_HEADER, None):
            token = self._get_xsrf_token()
            self._headers[self.XSRF_HEADER] = token

        payload = dict()
        payload['parameters'] = [
        {
            "name": "CAMUsername",
            "value": user,
        },
        {
            "name": "CAMPassword",
            "value": password,
        }
        ]

        if namespace:
            payload['parameters'].append({ "name": "CAMNamespace", "value": namespace })

        self.PUT(url, data=json.dumps(payload))
            

    def _get_xsrf_token(self):
        url = '/api/v1/session'
        response = self.GET(url)
        token = response.cookies.get(self.XSRF_COOKIE, None)
        if not token:
            raise RuntimeError('Could not extract XSRF token from headers')
        return token

    def GET(self, url: str, headers: Dict = None):
        return self._http.get(
            url=self._base_url + url, 
            headers={**self._headers, **headers} if headers else self._headers
        )
        
    def PUT(self, url: str, data: Union[str, bytes], headers: Dict = None):
        return self._http.put(
            url=self._base_url + url,
            data=data, 
            headers={**self._headers, **headers} if headers else self._headers
        )
    
    def PATCH(self, url: str, data: Union[str, bytes], headers: Dict = None):
        return self._http.patch(
            url=self._base_url + url,
            data=data, 
            headers={**self._headers, **headers} if headers else self._headers
        )

    def POST(self, url: str, data: Union[str, bytes], headers: Dict = None):
        return self._http.post(
            url=self._base_url + url,
            data=data, 
            headers={**self._headers, **headers} if headers else self._headers
        )

    def PUT(self, url: str, data: Union[str, bytes], headers: Dict = None):
        return self._http.put(
            url=self._base_url + url,
            data=data, 
            headers={**self._headers, **headers} if headers else self._headers
        )

    def DELETE(self, url: str, data: Union[str, bytes], headers: Dict = None):
        return self._http.delete(
            url=self._base_url + url,
            data=data, 
            headers={**self._headers, **headers} if headers else self._headers
        )