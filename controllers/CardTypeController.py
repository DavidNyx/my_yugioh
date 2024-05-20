import sys
sys.path.append('./')
from models.CardType import CardType

class CardTypeController(CardType):
    def __init__(self, card_type_id: int = None, card_type_name: str = None):
        super().__init__(card_type_id, card_type_name)
        
    def all(self, order='card_type_name', order_by='ASC', limit=0):
        return super().all(order, order_by, limit)
    
    def filter(self, card_type_id=None, card_type_name=None, order='card_type_name', order_by='ASC', limit=0):
        return super().filter(card_type_id, card_type_name, order, order_by, limit)
    
    def change_into(self, card_type_id=None):
        return super().change_into(card_type_id)
    
    def create(self, card_type_name):
        return super().create(card_type_name)

    def update(self, card_type_name, card_type_id=None):
        return super().update(card_type_name, card_type_id)
    
    def delete(self, card_type_id=None):
        return super().delete(card_type_id)