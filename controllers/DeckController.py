from datetime import datetime
import sys
sys.path.append('./')
from models.Database import DB
from models.Deck import Deck
import UserController

class DeckController(Deck):
    def __init__(self, deck_id: int=None, owner: UserController.User=None, created_at: datetime=None, updated_at: datetime=None):
        super().__init__(deck_id, owner, created_at, updated_at)
        
    def all(self):
        return super().all()
    
    def filter(self, deck_id=None, owner_id=None, created_at=None, updated_at=None, first=False, order_by='ASC'):
        return super().filter(deck_id, owner_id, created_at, updated_at, first, order_by)
    
    def create(self, owner_id):
        return super().create(owner_id)
    
    def update(self, deck_id=None, owner_id=None):
        return super().update(deck_id, owner_id)
    
    def delete(self, deck_id):
        return super().delete(deck_id)
    