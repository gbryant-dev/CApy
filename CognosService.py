from GroupService import GroupService
from RESTService import RESTService
from UserService import UserService

class CognosService:

  def __init__(self, **kwargs) -> None:
      self._cognos_rest = RESTService(**kwargs)
      self.groups = GroupService(self._cognos_rest)
      self.users = UserService(self._cognos_rest)