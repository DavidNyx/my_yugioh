import sys
sys.path.append('./')
from models.Card_Link import Card_Link

class Card_LinkController(Card_Link):
    def __init__(self, card_id: str = None, link_arrow_id: int = None):
        super().__init__(card_id, link_arrow_id)
    
    def all(self, order='card_id', order_by='ASC', limit=0):
        return super().all(order, order_by, limit)
    
    def filter(self, card_id=None, link_arrow_id=None, order='card_id', order_by='ASC', limit=0, empty=None):
        return super().filter(card_id, link_arrow_id, order, order_by, limit, empty)
    
    def change_into(self, card_id=None, link_arrow_id=None):
        return super().change_into(card_id, link_arrow_id)
    
    def create(self, card_id, link_arrow_id):
        return super().create(card_id, link_arrow_id)
    
    def delete(self, card_id=None, link_arrow_id=None):
        return super().delete(card_id, link_arrow_id)