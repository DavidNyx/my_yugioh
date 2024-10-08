import sys
sys.path.append('./')
from models.DeckType import DeckType

class DeckTypeController(DeckType):
    def __init__(self, deck_type_id: int = None, deck_type_name: str = None, min_size: int = None, max_size: int = None):
        super().__init__(deck_type_id, deck_type_name, min_size, max_size)
        
    def all(self, order='deck_type_name', order_by='ASC', limit=0):
        return super().all(order, order_by, limit)
    
    def filter(self, deck_type_id=None, deck_type_name=None, min_size=None, max_size=None, order='deck_type_name', order_by='ASC', limit=0):
        return super().filter(deck_type_id, deck_type_name, min_size, max_size, order, order_by, limit)
    
    def change_into(self, deck_type_id=None):
        return super().change_into(deck_type_id)
    
    def create(self, deck_type_name, min_size, max_size):
        return super().create(deck_type_name, min_size, max_size)
    
    def update(self, deck_type_id=None, deck_type_name=None, min_size=None, max_size=None):
        return super().update(deck_type_id, deck_type_name, min_size, max_size)
    
    def delete(self, deck_type_id=None):
        return super().delete(deck_type_id)

