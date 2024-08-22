import sys
sys.path.append('./')
from models.Database import DB

class CardType:
    def __init__(self, card_type_id:int=None, card_type_name:str=None):
        self.card_type_id = card_type_id
        self.card_type_name = card_type_name
        
    def all(self, order='card_type_name', order_by='ASC', limit=0):
        DB.connect()
        query = "SELECT * FROM `card_type`"
        query_result = DB.execute_query(query, order=order, order_by=order_by, limit=limit)
        DB.disconnect()
        
        if query_result is None:
            return None
        
        if limit == 0 or limit > 1:
            result = []
            for i in query_result:
                result.append(CardType(i[0], i[1]))
            return result
        elif limit == 1:
            return CardType(query_result[0], query_result[1])
        else:
            return None

    def filter(self, card_type_id=None, card_type_name=None, order='card_type_name', order_by='ASC', limit=0):
        if card_type_id is None and card_type_name is None:
            return CardType().all()
        
        DB.connect()
        query = f"""SELECT * FROM `card_type` WHERE {"`card_type_id` = " + str(card_type_id) if card_type_id is not None else ""}{" AND " if card_type_id is not None and card_type_name is not None else ""}{"`card_type_name` = '" + card_type_name + "'" if card_type_name is not None else ""}"""
        query_result = DB.execute_query(query, order=order, order_by=order_by, limit=limit)
        DB.disconnect()
        
        if query_result is None:
            return None
        
        if limit == 0 or limit > 1:
            result = []
            for i in query_result:
                result.append(CardType(i[0], i[1]))
            return result
        elif limit == 1:
            return CardType(query_result[0], query_result[1])
        else:
            return None
    
    def change_into(self, card_type_id=None):
        if card_type_id is None:
            self.card_type_id = None
            self.card_type_name = None
            return self
    
        DB.connect()
        query = f"SELECT * FROM `card_type` WHERE `card_type_id` = {str(card_type_id)}"
        query_result = DB.execute_query(query, limit=1)
        DB.disconnect()
        
        if query_result is None:
            return None
        
        self.card_type_id = query_result[0]
        self.card_type_name = query_result[1]
        
        return self

    def create(self, card_type_name):
        DB.connect()
        query = f"INSERT INTO `card_type`(`card_type_name`) VALUES ('{card_type_name}')"
        query_result = DB.execute_query(query, limit=-1)
        DB.disconnect()
        
        if query_result is None:
            return None

        return self.change_into(query_result)
        
                
    def update(self, card_type_name, card_type_id=None):
        if card_type_id is not None or self.card_type_id is not None:
            DB.connect()
            query = f"UPDATE `card_type` SET `card_type_name`= '{card_type_name}' WHERE `card_type_id` = {str(card_type_id) if card_type_id is not None else str(self.card_type_id)}"
            query_result = DB.execute_query(query)
            DB.disconnect()
            
            if query_result is None:
                return None
            
            return self.change_into(card_type_id=card_type_id if card_type_id is not None else self.card_type_id)
        
    def delete(self, card_type_id=None):
        if card_type_id is not None or self.card_type_id is not None:
            DB.connect()
            query = f"DELETE FROM `card_type` WHERE `card_type_id` = {str(card_type_id) if card_type_id is not None else str(self.card_type_id)}"
            query_result = DB.execute_query(query)
            DB.disconnect()
            
            if query_result is None:
                return None
            
            return self.change_into()
            