import sys
sys.path.append('./')
from models.Card_Version import Card_Version

class Card_VersionController(Card_Version):
    def __init__(self, card_id: str = None, version_id: int = None, card_limit: int = None):
        super().__init__(card_id, version_id, card_limit)
    
    def all(self, order='card_limit', order_by='ASC', limit=0):
        return super().all(order, order_by, limit)
    
    def filter(self, card_id=None, version_id=None, card_limit=None, order='card_limit', order_by='ASC', limit=0, empty=None):
        return super().filter(card_id, version_id, card_limit, order, order_by, limit, empty)
    
    def change_into(self, card_id=None, version_id=None):
        return super().change_into(card_id, version_id)
    
    def create(self, card_id, version_id, card_limit):
        return super().create(card_id, version_id, card_limit)
    
    def update(self, card_id=None, version_id=None, card_limit=None):
        return super().update(card_id, version_id, card_limit)
    
    def delete(self, card_id=None, version_id=None):
        return super().delete(card_id, version_id)