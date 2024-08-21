from datetime import datetime
import sys
sys.path.append('./')
from models.Deck import Deck

class DeckController(Deck):
    def __init__(self, deck_id: int = None, deck_name: str = None, owner_id: str = None, created_at: datetime = None, updated_at: datetime = None, card_decks: list = []):
        super().__init__(deck_id, deck_name, owner_id, created_at, updated_at, card_decks)
        
    def all(self, order='deck_name', order_by='ASC', limit=0):
        return super().all(order, order_by, limit)
    
    def filter(self, deck_id=None, deck_name=None, owner_id=None, created_at=None, updated_at=None, limit=0, order='deck_id', order_by='ASC'):
        return super().filter(deck_id, deck_name, owner_id, created_at, updated_at, limit, order, order_by)
    
    def change_into(self, deck_id=None):
        return super().change_into(deck_id)
    
    def create(self, deck_name, owner_id):
        return super().create(deck_name, owner_id)
    
    def update(self, deck_id=None, deck_name=None, owner_id=None):
        return super().update(deck_id, deck_name, owner_id)
    
    def delete(self, deck_id):
        return super().delete(deck_id)
    