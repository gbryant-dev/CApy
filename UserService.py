from RESTService import RESTService
from requests import Response

class UserService:
  def __init__(self, rest: RESTService) -> None:
      self._rest = rest

  def get_user(self, id: str) -> Response:
      url = "/api/v1/users/{}".format(id)
      response = self._rest.GET(url)
      return response.json()

  def get_users(self, id: str) -> Response:
      url = "/api/v1/users?identifier={}".format(id)
      response = self._rest.GET(url)
      return [user for user in response.json()['users']]