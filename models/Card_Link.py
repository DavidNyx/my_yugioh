import sys
import importlib
sys.path.append('./')
from models.Database import DB
try:
    Card = importlib.import_module("Card")
except:
    Card = importlib.import_module("models.Card")
try:
    LinkArrow = importlib.import_module("LinkArrow")
except:
    LinkArrow = importlib.import_module("models.LinkArrow")

class Card_Link:
    def __init__(self, card_id:str=None, link_arrow_id:int=None):
        self.card = Card.Card().change_into(card_id=card_id)
        self.link_arrow = LinkArrow.LinkArrow().change_into(link_arrow_id=link_arrow_id)
        
    def all(self, order='card_id', order_by='ASC', limit=0):
        DB.connect()
        query = f"SELECT * FROM `card_link`"
        query_result = DB.execute_query(query, order=order, order_by=order_by, limit=limit)
        DB.disconnect()
        
        if query_result is None:
            return None
        
        if limit == 0 or limit > 1:
            result = []
            for i in query_result:
                result.append(Card_Link(i[0], i[1]))
            return result
        elif limit == 1:
            return Card_Link(query_result[0], query_result[1])
        else:
            return None
    
    def filter(self, card_id=None, link_arrow_id=None, order='card_id', order_by='ASC', limit=0, empty=None):
        if card_id is None and link_arrow_id is None:
            return Card_Link().all()
        
        DB.connect()
        query = f"""SELECT * FROM `card_link` WHERE {"`card_id` = '" + card_id + "'" if card_id is not None else ""}{" AND " if card_id is not None and link_arrow_id is not None else ""}{"`link_arrow_id` = " + str(link_arrow_id) if link_arrow_id is not None else ""}"""
        query_result = DB.execute_query(query, order=order, order_by=order_by, limit=limit)
        DB.disconnect()
        
        if query_result is None:
            return None
        
        if limit == 0 or limit > 1:
            result = []
            for i in query_result:
                result.append(Card_Link(i[0] if empty != 'card' else None, i[1] if empty != 'link' else None))
            return result
        elif limit == 1:
            return Card_Link(query_result[0] if empty != 'card' else None, query_result[1] if empty != 'link' else None)
        else:
            return None
        
    def change_into(self, card_id=None, link_arrow_id=None):
        if card_id is None or link_arrow_id is None:
            self.card = None
            self.link_arrow = None
            return self
        
        DB.connect()
        query = f"""SELECT * FROM `card_link` WHERE `card_id` = '{card_id}' AND `link_arrow_id` = {str(link_arrow_id)}"""
        query_result = DB.execute_query(query, limit=1)
        DB.disconnect()
        
        if query_result is None:
            return None
        
        self.card = Card.Card().change_into(card_id=query_result[0])
        self.link_arrow = LinkArrow.LinkArrow().change_into(link_arrow_id=query_result[1])
        
        return self
    
    def create(self, card_id, link_arrow_id):
        DB.connect()
        query = f"INSERT INTO `card_link`(`card_id`, `link_arrow_id`) VALUES {card_id}, {str(link_arrow_id)})"
        query_result = DB.execute_query(query)
        DB.disconnect()
        
        if query_result is None:
            return None
        
        return self.change_into(card_id=card_id, link_arrow_id=link_arrow_id)
        
    def delete(self, card_id=None, link_arrow_id=None):
        if card_id is not None or link_arrow_id is not None:
            DB.connect()
            query = f"""DELETE FROM `card_link` WHERE {"`card_id` = '" + card_id + "'" if card_id is not None else ""}{" AND " if card_id is not None and link_arrow_id is not None else ""}{"`link_arrow_id` = " + str(link_arrow_id) if link_arrow_id is not None else ""}"""
            query_result = DB.execute_query(query)
            DB.disconnect()
        elif self.card.card_id is not None and self.link_arrow.link_arrow_id is not None:
            DB.connect()
            query = f"DELETE FROM `card_link` WHERE `card_id` = '{self.card.card_id}' AND `link_arrow_id` = {str(self.link_arrow.link_arrow_id)}"
            query_result = DB.execute_query(query)
            DB.disconnect()
        
        if query_result is None:
            return None
        
        return self.change_into()