import sys
sys.path.append('./')
from models.Database import DB

class DeckType:
    def __init__(self, deck_type_id:int=None, deck_type_name:str=None):
        self.deck_type_id = deck_type_id
        self.deck_type_name = deck_type_name
        
    def all(self, order='deck_type_name', order_by='ASC', limit=0):
        DB.connect()
        query = "SELECT * FROM `deck_type`"
        query_result = DB.execute_query(query, order=order, order_by=order_by,limit=limit)
        DB.disconnect()

        if limit == 0 or limit > 1:
            result = []
            for i in query_result:
                result.append(DeckType(i[0], i[1]))
            return result
        elif limit == 1:
            return DeckType(query_result[0], query_result[1])
        else:
            return None

    def filter(self, deck_type_id=None, deck_type_name=None, order='deck_type_name', order_by='ASC', limit=0):
        if deck_type_id is None and deck_type_name is None:
            return all()
        
        DB.connect()
        query = f"""SELECT * FROM `deck_type` WHERE {"`deck_type_id` = " + str(deck_type_id) if deck_type_id is not None else ""}{" AND " if deck_type_id is not None and deck_type_name is not None else ""}{"`deck_type_name` = '" + deck_type_name + "'" if deck_type_name is not None else ""}"""
        query_result = DB.execute_query(query, order=order, order_by=order_by,limit=limit)
        DB.disconnect()
        
        if limit == 0 or limit > 1:
            result = []
            for i in query_result:
                result.append(DeckType(i[0], i[1]))
            return result
        elif limit == 1:
            return DeckType(query_result[0], query_result[1])
        else:
            return None
        
    def change_into(self, deck_type_id=None):
        if deck_type_id is None:
            self.deck_type_id = None
            self.deck_type_name = None
            return self
        
        DB.connect()
        query = f"SELECT * FROM `deck_type` WHERE `deck_type_id` = {str(deck_type_id)}"
        query_result = DB.execute_query(query, limit=1)
        DB.disconnect()
        
        self.deck_type_id = query_result[0]
        self.deck_type_name = query_result[1]
        
        return self

    def create(self, deck_type_name):
        DB.connect()
        query = f"INSERT INTO `deck_type`(`deck_type_name`) VALUES ('{deck_type_name}')"
        query_result = DB.execute_query(query, limit=-1)
        DB.disconnect()
        
        if query_result == False:
            return None

        return self.change_into(query_result)
        
                
    def update(self, deck_type_name, deck_type_id=None):
        if deck_type_id is not None or self.deck_type_id is not None:
            DB.connect()
            query = f"UPDATE `deck_type` SET `deck_type_name`= '{deck_type_name}' WHERE `deck_type_id` = {str(deck_type_id) if deck_type_id is not None else str(self.deck_type_id)}"
            query_result = DB.execute_query(query)
            DB.disconnect()
            
            if query_result == False:
                return None
            
            return self.change_into(deck_type_id=deck_type_id if deck_type_id is not None else self.deck_type_id)
        
    def delete(self, deck_type_id=None):
        if deck_type_id is not None or self.deck_type_id is not None:
            DB.connect()
            query = f"DELETE FROM `deck_type` WHERE `deck_type_id` = {str(deck_type_id) if deck_type_id is not None else str(self.deck_type_id)}"
            query_result = DB.execute_query(query)
            DB.disconnect()
            
            return self.change_into()
            