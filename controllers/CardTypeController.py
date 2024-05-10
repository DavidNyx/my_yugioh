import sys
sys.path.append('./')
from models.CardType import CardType

class CardTypeController(CardType):
    def __init__(self, card_type_id: int = None, card_type_name: str = None):
        super().__init__(card_type_id, card_type_name)
        
    def all(self):
        return super().all()
    
    def filter(self, card_type_id=None, card_type_name=None, first=False):
        return super().filter(card_type_id, card_type_name, first)
    
    def create(self, card_type_name):
        return super().create(card_type_name)
    
    def update(self, card_type_name, card_type_id=None):
        return super().update(card_type_name, card_type_id)
    
    def delete(self, card_type_id=None):
        return super().delete(card_type_id)

