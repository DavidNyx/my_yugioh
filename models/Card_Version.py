import sys
import importlib
sys.path.append('./')
# from models.Card import Card
# from models.Version import Version
from models.Database import DB
try:
    Card = importlib.import_module("Card")
except:
    Card = importlib.import_module("models.Card")
try:
    Version = importlib.import_module("Version")
except:
    Version = importlib.import_module("models.Version")

class Card_Version():
    def __init__(self, card_id:str=None, version_id:int=None, card_limit:int=None):
        self.card = Card.Card().change_into(card_id=card_id)
        self.version = Version.Version().change_into(version_id=version_id)
        self.card_limit = card_limit
        
    def all(self, order='card_limit', order_by='ASC', limit=0):
        DB.connect()
        query = f"SELECT * FROM `card_version`"
        query_result = DB.execute_query(query, order=order, order_by=order_by, limit=limit)
        DB.disconnect()
        
        if query_result is None:
            return None
        
        if limit == 0 or limit > 1:
            result = []
            for i in query_result:
                result.append(Card_Version(i[0], i[1], i[2]))
            return result
        elif limit == 1:
            return Card_Version(query_result[0], query_result[1], query_result[2])
        else:
            return None
    
    def filter(self, card_id=None, version_id=None, card_limit=None, order='card_limit', order_by='ASC', limit=0, empty=None):
        if card_id is None and version_id is None and card_limit is None:
            return all()
        
        DB.connect()
        query = f"""SELECT * FROM `card_version` WHERE {"`card_id` = '" + card_id + "'" if card_id is not None else ""}{" AND " if card_id is not None and version_id is not None else ""}{"`version_id` = " + str(version_id) if version_id is not None else ""}{" AND " if (card_id is not None or version_id is not None) and card_limit is not None else ""}{"`card_limit` = " + str(card_limit) if card_limit is not None else ""}"""
        query_result = DB.execute_query(query, order=order, order_by=order_by, limit=limit)
        DB.disconnect()
        
        if query_result is None:
            return None
        
        if limit == 0 or limit > 1:
            result = []
            for i in query_result:
                result.append(Card_Version(i[0] if empty != 'card' else None, i[1] if empty != 'version' else None, i[2]))
            return result
        elif limit == 1:
            return Card_Version(query_result[0] if empty != 'card' else None, query_result[1] if empty != 'version' else None, query_result[2])
        else:
            return None
        
    def change_into(self, card_id=None, version_id=None):
        if card_id is None or version_id is None:
            self.card_id = None
            self.version_id = None
            self.card_limit = None
            return self
        
        DB.connect()
        query = f"""SELECT * FROM `card_version` WHERE `card_id` = '{card_id}' AND `version_id` = {str(version_id)}"""
        query_result = DB.execute_query(query, limit=1)
        DB.disconnect()
        
        if query_result is None:
            return None
        
        self.card = Card.Card().change_into(card_id=card_id)
        self.version = Version.Version().change_into(version_id=version_id)
        self.card_limit = query_result[2]
        
        return self
    
    def create(self, card_id, version_id, card_limit):
        DB.connect()
        query = f"INSERT INTO `card_version`(`card_id`, `version_id`, `card_limit`) VALUES ({str(card_id)}, {str(version_id)}, {str(card_limit)})"
        query_result = DB.execute_query(query)
        DB.disconnect()
        
        if query_result is None:
            return None
        
        return self.change_into(card_id=card_id, version_id=version_id)
    
    def update(self, card_id=None, version_id=None, card_limit=None):
        if (card_id is not None and version_id is not None) or (self.card_id is not None and self.version_id is not None):
            DB.connect()
            query = f"UPDATE `card_version` SET `card_limit`= {str(card_limit)} WHERE `card_id` = '{card_id if card_id is not None else self.card_id}' AND `version_id` = {str(version_id) if version_id is not None else str(self.version_id)}"
            query_result = DB.execute_query(query)
            DB.disconnect()
            
            if query_result is None:
                return None
            
            return self.change_into(card_id=card_id if card_id is not None else self.card_id, version_id=version_id if version_id is not None else self.version_id)
        
    def delete(self, card_id=None, version_id=None):
        if card_id is not None or version_id is not None:
            DB.connect()
            query = f"""DELETE FROM `card_version` WHERE {"`card_id` = '" + card_id + "'" if card_id is not None else ""}{" AND " if card_id is not None and version_id is not None else ""}{"`version_id` = " + str(version_id) if version_id is not None else ""}"""
            query_result = DB.execute_query(query)
            DB.disconnect()
        elif self.card_id is not None and self.version_id is not None:
            DB.connect()
            query = f"DELETE FROM `card_version` WHERE `card_id` = '{self.card_id}' AND `version_id` = {str(self.version_id)}"
            query_result = DB.execute_query(query)
            DB.disconnect()
        
        if query_result is None:
            return None
        
        return self.change_into()