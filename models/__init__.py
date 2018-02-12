from .engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City

storage = FileStorage()
c_manager = {'User': User, 'BaseModel' : BaseModel, 'State' : State, 'City': City}
storage.reload()
