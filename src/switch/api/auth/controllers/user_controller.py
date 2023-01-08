import logging
from switch.api.auth.models.user import User
from switch.utils import SwitchRestClient

_logger = logging.getLogger(__name__)

BASE_PATH="/user"

class UserController:
  def __init__(self, client: SwitchRestClient):
    self.client = client
  
  async def get_user(self) -> User:
    response= await self.client.get(f"{BASE_PATH}")
    return User.from_json(response.data)