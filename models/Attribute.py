import sys
sys.path.append('./')
from models.Database import DB

class Attribute:
    def __init__(self, attr_id:int=None, attr_name:str=None):
        self.attr_id = attr_id
        self.attr_name = attr_name
        
    def all(self):
        result = []
        DB.connect()
        query = "SELECT * FROM `attribute`"
        query_result = DB.execute_query(query)
        DB.disconnect()

        for i in query_result:
            result.append(Attribute(i[0], i[1]))
        
        return result

    def filter(self, attr_id=None, attr_name=None, first=False):
        if attr_id is None and attr_name is None:
            return all()
        
        result = []
        DB.connect()
        query = f"""SELECT * FROM `attribute` WHERE {"`attr_id` = " + str(attr_id) if attr_id is not None else ""} {" AND " if attr_id is not None and attr_name is not None else ""} {"`attr_name` = '" + attr_name + "'" if attr_name is not None else ""} {" LIMIT 1" if first == True else ""}"""
        query_result = DB.execute_query(query)
        DB.disconnect()
        
        for i in query_result:
            result.append(Attribute(i[0], i[1]))
        
        if first == True:
            return result[0]
        return result
    
    def change_into(self, attr_id):
        DB.connect()
        query = f"SELECT * FROM `attribute` WHERE `attr_id` = {str(attr_id)}"
        query_result = DB.execute_query(query)
        DB.disconnect()
        
        self.attr_id = query_result[0][0]
        self.attr_name = query_result[0][1]
        
        return self

    def create(self, attr_name):
        DB.connect()
        query = f"INSERT INTO `attribute`(`attr_name`) VALUES ('{attr_name}')"
        query_result = DB.execute_query(query)
        DB.disconnect()
        
        if query_result == False:
            return None

        return self.change_into(query_result)
        
                
    def update(self, attr_name, attr_id=None):
        if attr_id is not None or self.attr_id is not None:
            DB.connect()
            query = f"UPDATE `attribute` SET `attr_name`= '{attr_name}' WHERE `attr_id` = {str(attr_id) if attr_id is not None else str(self.attr_id)}"
            query_result = DB.execute_query(query)
            DB.disconnect()
            
            if query_result == False:
                return None
            
            return self.change_into(attr_id=attr_id if attr_id is not None else self.attr_id)
        
    def delete(self, attr_id=None):
        if attr_id is not None or self.attr_id is not None:
            DB.connect()
            query = f"DELETE FROM `attribute` WHERE `attr_id` = {str(attr_id) if attr_id is not None else str(self.attr_id)}"
            query_result = DB.execute_query(query)
            DB.disconnect()
            
            return None
            