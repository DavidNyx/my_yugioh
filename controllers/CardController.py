import sys
sys.path.append('./')
from models.Card import Card

class CardController(Card):
    def __init__(self, card_id: str = None, card_name: str = None, desc: str = None, pendulum_effect: str = None, level_rank: int = None, scale: int = None, attack: int = None, defense: int = None, category_id: int = None, card_type_id: int = None, attr_id: int = None, card_versions: list = [], card_links: list = [], card_subcategories: list = [], card_decks: list = []):
        super().__init__(card_id, card_name, desc, pendulum_effect, level_rank, scale, attack, defense, category_id, card_type_id, attr_id, card_versions, card_links, card_subcategories, card_decks)
    
    def all(self, order='card_name', order_by='ASC', limit=0):
        return super().all(order, order_by, limit)

    def filter(self, card_id=None, card_name=None, desc=None, pendulum_effect=None, level_rank=None, scale=None, attack=None, defense=None, category_id=None, card_type_id=None, attr_id=None, order='card_name', order_by='ASC', limit=0):
        return super().filter(card_id, card_name, desc, pendulum_effect, level_rank, scale, attack, defense, category_id, card_type_id, attr_id, order, order_by, limit)
    
    def change_into(self, card_id=None):
        return super().change_into(card_id)
    
    def create(self, card_id, card_name, desc, category_id, card_type_id, pendulum_effect=None, level_rank=None, scale=None, attack=None, defense=None, attr_id=None):
        return super().create(card_id, card_name, desc, category_id, card_type_id, pendulum_effect, level_rank, scale, attack, defense, attr_id)
    
    def update(self, card_id=None, card_name=None, desc=None, pendulum_effect=None, level_rank=None, scale=None, attack=None, defense=None, category_id=None, card_type_id=None, attr_id=None):
        return super().update(card_id, card_name, desc, pendulum_effect, level_rank, scale, attack, defense, category_id, card_type_id, attr_id)
    
    def delete(self, card_id=None):
        return super().delete(card_id)