import sys
import importlib
sys.path.append('./')
from models.Database import DB
try:
    Card = importlib.import_module("Card")
except:
    Card = importlib.import_module("models.Card")
try:
    SubCategory = importlib.import_module("SubCategory")
except:
    SubCategory = importlib.import_module("models.SubCategory")

class Card_SubCategory:
    def __init__(self, card_id:str=None, subcategory_id:int=None, empty=None):
        if empty != 'all':
            self.card = Card.Card().change_into(card_id=card_id, empty=empty)
            self.subcategory = SubCategory.SubCategory().change_into(subcategory_id=subcategory_id, empty=empty)
        else:
            self.card = Card.Card().change_into(card_id=card_id, empty='subcategory')
            self.subcategory = SubCategory.SubCategory().change_into(subcategory_id=subcategory_id, empty='card')
        
    def all(self, order='card_id', order_by='ASC', limit=0):
        DB.connect()
        query = f"SELECT * FROM `card_subcategory`"
        query_result = DB.execute_query(query, order=order, order_by=order_by, limit=limit)
        DB.disconnect()
        
        if query_result is None:
            return None
        
        if limit == 0 or limit > 1:
            result = []
            for i in query_result:
                result.append(Card_SubCategory(i[0], i[1]))
            return result
        elif limit == 1:
            return Card_SubCategory(query_result[0], query_result[1])
        else:
            return None
    
    def filter(self, card_id=None, subcategory_id=None, order='card_id', order_by='ASC', limit=0, empty=None):
        if card_id is None and subcategory_id is None:
            return Card_SubCategory().all()
        
        DB.connect()
        query = f"""SELECT * FROM `card_subcategory` WHERE {"`card_id` = '" + card_id + "'" if card_id is not None else ""}{" AND " if card_id is not None and subcategory_id is not None else ""}{"`subcategory_id` = " + str(subcategory_id) if subcategory_id is not None else ""}"""
        query_result = DB.execute_query(query, order=order, order_by=order_by, limit=limit)
        DB.disconnect()
        
        if query_result is None:
            return None
        
        if limit == 0 or limit > 1:
            result = []
            for i in query_result:
                result.append(Card_SubCategory(i[0] if empty != 'card' else None, i[1] if empty != 'subcategory' else None, empty))
            return result
        elif limit == 1:
            return Card_SubCategory(query_result[0] if empty != 'card' else None, query_result[1] if empty != 'subcategory' else None, empty)
        else:
            return None
        
    def change_into(self, card_id=None, subcategory_id=None):
        if card_id is None or subcategory_id is None:
            self.card = None
            self.subcategory = None
            return self
        
        DB.connect()
        query = f"""SELECT * FROM `card_subcategory` WHERE `card_id` = '{card_id}' AND `subcategory_id` = {str(subcategory_id)}"""
        query_result = DB.execute_query(query, limit=1)
        DB.disconnect()
        
        if query_result is None:
            return None
        
        self.card = Card.Card().change_into(card_id=query_result[0])
        self.subcategory = SubCategory.SubCategory().change_into(subcategory_id=query_result[1])
        
        return self
    
    def create(self, card_id, subcategory_id):
        DB.connect()
        query = f"INSERT INTO `card_subcategory`(`card_id`, `subcategory_id`) VALUES ({card_id}, {str(subcategory_id)})"
        query_result = DB.execute_query(query)
        DB.disconnect()
        
        if query_result is None:
            return None
        
        return self.change_into(card_id=card_id, subcategory_id=subcategory_id)
        
    def delete(self, card_id=None, subcategory_id=None):
        if card_id is not None or subcategory_id is not None:
            DB.connect()
            query = f"""DELETE FROM `card_subcategory` WHERE {"`card_id` = '" + card_id + "'" if card_id is not None else ""}{" AND " if card_id is not None and subcategory_id is not None else ""}{"`subcategory_id` = " + str(subcategory_id) if subcategory_id is not None else ""}"""
            query_result = DB.execute_query(query)
            DB.disconnect()
        elif self.card.card_id is not None and self.subcategory.subcategory_id is not None:
            DB.connect()
            query = f"DELETE FROM `card_subcategory` WHERE `card_id` = '{self.card.card_id}' AND `subcategory_id` = {str(self.subcategory.subcategory_id)}"
            query_result = DB.execute_query(query)
            DB.disconnect()
        
        if query_result is None:
            return None
        
        return self.change_into()