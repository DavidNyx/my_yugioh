import sys
sys.path.append('./')
from models.DeckType import DeckType

class DeckTypeController(DeckType):
    def __init__(self, deck_type_id: int = None, deck_type_name: str = None):
        super().__init__(deck_type_id, deck_type_name)
        
    def all(self):
        return super().all()
    
    def filter(self, deck_type_id=None, deck_type_name=None, first=False):
        return super().filter(deck_type_id, deck_type_name, first)
    
    def create(self, deck_type_name):
        return super().create(deck_type_name)
    
    def update(self, deck_type_name, deck_type_id=None):
        return super().update(deck_type_name, deck_type_id)
    
    def delete(self, deck_type_id=None):
        return super().delete(deck_type_id)

