import sys
sys.path.append('./')
from models.Database import DB

class DeckType:
    def __init__(self, deck_type_id:int=None, deck_type_name:str=None):
        self.deck_type_id = deck_type_id
        self.deck_type_name = deck_type_name
        
    def all(self):
        result = []
        DB.connect()
        query = "SELECT * FROM `deck_type`"
        query_result = DB.execute_query(query)
        DB.disconnect()

        for i in query_result:
            result.append(DeckType(i[0], i[1]))
        
        return result

    def filter(self, deck_type_id=None, deck_type_name=None, first=False):
        if deck_type_id is None and deck_type_name is None:
            return all()
        
        result = []
        DB.connect()
        query = f"""SELECT * FROM `deck_type` WHERE {"`deck_type_id` = " + str(deck_type_id) if deck_type_id is not None else ""} {" AND " if deck_type_id is not None and deck_type_name is not None else ""} {"`deck_type_name` = '" + deck_type_name + "'" if deck_type_name is not None else ""} {" LIMIT 1" if first == True else ""}"""
        query_result = DB.execute_query(query)
        DB.disconnect()
        
        for i in query_result:
            result.append(DeckType(i[0], i[1]))
        
        if first == True:
            return result[0]
        return result
    
    def change_into(self, deck_type_id):
        DB.connect()
        query = f"SELECT * FROM `deck_type` WHERE `deck_type_id` = {str(deck_type_id)}"
        query_result = DB.execute_query(query)
        DB.disconnect()
        
        self.deck_type_id = query_result[0][0]
        self.deck_type_name = query_result[0][1]
        
        return self

    def create(self, deck_type_name):
        DB.connect()
        query = f"INSERT INTO `deck_type`(`deck_type_name`) VALUES ('{deck_type_name}')"
        query_result = DB.execute_query(query)
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
            
            return None
            