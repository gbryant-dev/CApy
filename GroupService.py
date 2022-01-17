from typing import Optional, Tuple, List
import RestClient
from requests import Response
import json

class GroupService:
  
  def __init__(self, **kwargs):
      self._rest = RestClient(**kwargs)


  def get_group(self, id: str) -> Response:
      url = "/api/v1/groups/{}".format(id)
      response = self._rest.GET(url)
      return response.json()

  def get_groups(self, parent_id: Optional[str] = None) -> List:
      url = "/api/v1/groups{parent_id}".format(parent_id=f"?parent_id={parent_id}" if parent_id else "")
      response = self._rest.GET(url)
      return [group for group in response.json()['groups']]

  def get_group_members(self, id: str) -> Tuple[List, List]:
      url = "/api/v1/groups/{}/members".format(id)
      json = self._rest.GET(url).json()
      users, groups = json['users'], json['groups']
      return users, groups

  def add_member_to_group(self, group_id: str, user_ids: List[str] = None, group_ids: List[str] = None) -> Response:
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

      return self._rest.POST(url, data=json.dumps(payload))

  def delete_member_from_group(self, group_id: str, member_type: str, member_id: str) -> Response:
      url = "/api/v1/groups/{}/members/{}/{}".format(self, group_id, member_type, member_id)
      return self._rest.DELETE(url)