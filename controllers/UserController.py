import datetime
import sys
sys.path.append('./')
from models.User import User

class UserController(User):
    def __init__(self, username:str=None, password:str=None, created_at:datetime.datetime=None):
        super().__init__(username, password, created_at)
    
    def all(self):
        return super().all()
    
    def filter(self, username=None, created_at=None, first=False):
        return super().filter(username, created_at, first)
        
    def change_into(self, username):
        return super().change_into(username)
        
    def create(self, username, password):
        return super().create(username, password)
    
    def update(self, password, username=None):
        return super().update(password, username)
    
    def delete(self, username=None):
        return super().delete(username)
        