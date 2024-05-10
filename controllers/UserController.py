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
        
    def create(self, username, password):
        if super().create(username, password) == True:
            return super().filter(username=username, first=True)
        return None
    
    def update(self, password, username=None):
        if super().update(password, username) == True:
            return  super().filter(username=username, first=True)
        return None
    
    def delete(self, username=None):
        super().delete(username)
        return None
    

a =User()
print(a.create("admin","1"))