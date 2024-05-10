import datetime
import sys
sys.path.append('./')
from models.User import User

class UserController(User):
    def __init__(self, user_id: int = None, username: str = None, password: str = None, created_at: datetime.datetime = None):
        super().__init__(user_id, username, password, created_at)
    
    def all(self):
        return super().all()
    
    def filter(self, user_id=None, username=None, created_at=None, first=False):
        return super().filter(user_id, username, created_at, first)
    
    def change_into(self, user_id):
        return super().change_into(user_id)
        
    def create(self, username, password):
        return super().create(username, password)
    
    def update(self, password=None, username=None, user_id=None):
        return super().update(password, username, user_id)
    
    def delete(self, user_id=None):
        return super().delete(user_id)
        
