from datetime import datetime
import sys
sys.path.append('./')
from models.Database import DB
from models.Deck import Deck
import UserController

class DeckController(Deck):
    def __init__(self, deck_id: int, owner: UserController.User, created_at: datetime, updated_at: datetime):
        super().__init__(deck_id, owner, created_at, updated_at)
        
    def all(self):
        return super().all()