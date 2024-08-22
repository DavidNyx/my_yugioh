import sys
sys.path.append('./')
from models.Card_Deck import Card_Deck

class Card_DeckController(Card_Deck):
    def __init__(self, card_id: str = None, deck_id: int = None, deck_type_id: int = None, number_of_copies: int = 0):
        super().__init__(card_id, deck_id, deck_type_id, number_of_copies)
    
    def all(self, order='card_id', order_by='ASC', limit=0):
        return super().all(order, order_by, limit)
    
    def filter(self, card_id=None, deck_id=None, deck_type_id=None, order='card_id', order_by='ASC', limit=0, empty=None):
        return super().filter(card_id, deck_id, deck_type_id, order, order_by, limit, empty)
    
    def change_into(self, card_id=None, deck_id=None, deck_type_id=None, number_of_copies=0):
        return super().change_into(card_id, deck_id, deck_type_id, number_of_copies)
    
    def create(self, card_id, deck_id, deck_type_id, number_of_copies):
        return super().create(card_id, deck_id, deck_type_id, number_of_copies)
    
    def update(self, card_id=None, deck_id=None, deck_type_id=None, number_of_copies=0):
        return super().update(card_id, deck_id, deck_type_id, number_of_copies)
    
    def delete(self, card_id=None, deck_id=None, deck_type_id=None):
        return super().delete(card_id, deck_id, deck_type_id)