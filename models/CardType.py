import sys
sys.path.append('./')
from models.Database import DB

class CardType:
    def __init__(self, card_type_id:int=None, card_type_name:str=None):
        self.card_type_id = card_type_id
        self.card_type_name = card_type_name
        
    def all(self):
        result = []
        DB.connect()
        query = "SELECT * FROM `card_type`"
        query_result = DB.execute_query(query)
        DB.disconnect()

        for i in query_result:
            result.append(CardType(i[0], i[1]))
        
        return result

    def filter(self, card_type_id=None, card_type_name=None, first=False):
        if card_type_id is None and card_type_name is None:
            return all()
        
        result = []
        DB.connect()
        query = f"""SELECT * FROM `card_type` WHERE {"`card_type_id` = " + str(card_type_id) if card_type_id is not None else ""} {" AND " if card_type_id is not None and card_type_name is not None else ""} {"`card_type_name` = '" + card_type_name + "'" if card_type_name is not None else ""} {" LIMIT 1" if first == True else ""}"""
        query_result = DB.execute_query(query)
        DB.disconnect()
        
        for i in query_result:
            result.append(CardType(i[0], i[1]))
        
        if first == True:
            return result[0]
        return result
    
    def change_into(self, card_type_id):
        DB.connect()
        query = f"SELECT * FROM `card_type` WHERE `card_type_id` = {str(card_type_id)}"
        query_result = DB.execute_query(query)
        DB.disconnect()
        
        self.card_type_id = query_result[0][0]
        self.card_type_name = query_result[0][1]
        
        return self

    def create(self, card_type_name):
        DB.connect()
        query = f"INSERT INTO `card_type`(`card_type_name`) VALUES ('{card_type_name}')"
        query_result = DB.execute_query(query)
        DB.disconnect()
        
        if query_result == False:
            return None

        return self.change_into(query_result)
        
                
    def update(self, card_type_name, card_type_id=None):
        if card_type_id is not None or self.card_type_id is not None:
            DB.connect()
            query = f"UPDATE `card_type` SET `card_type_name`= '{card_type_name}' WHERE `card_type_id` = {str(card_type_id) if card_type_id is not None else str(self.card_type_id)}"
            query_result = DB.execute_query(query)
            DB.disconnect()
            
            if query_result == False:
                return None
            
            return self.change_into(card_type_id=card_type_id if card_type_id is not None else self.card_type_id)
        
    def delete(self, card_type_id=None):
        if card_type_id is not None or self.card_type_id is not None:
            DB.connect()
            query = f"DELETE FROM `card_type` WHERE `card_type_id` = {str(card_type_id) if card_type_id is not None else str(self.card_type_id)}"
            query_result = DB.execute_query(query)
            DB.disconnect()
            
            return None
            