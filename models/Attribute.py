import sys
sys.path.append('./')
from models.Database import DB

class Attribute:
    def __init__(self, attr_id:int=None, attr_name:str=None):
        self.attr_id = attr_id
        self.attr_name = attr_name
        
    def all(self, order='attr_name', order_by='ASC', limit=0):
        DB.connect()
        query = "SELECT * FROM `attribute`"
        query_result = DB.execute_query(query, order=order, order_by=order_by, limit=limit)
        DB.disconnect()
        
        if query_result is None:
            return None

        if limit == 0 or limit > 1:
            result = []
            for i in query_result:
                result.append(Attribute(i[0], i[1]))
            return result
        elif limit == 1:
            return Attribute(query_result[0], query_result[1])
        else:
            return None
        
    def filter(self, attr_id=None, attr_name=None, order='attr_name', order_by='ASC', limit=0):
        if attr_id is None and attr_name is None:
            return all()
        
        DB.connect()
        query = f"""SELECT * FROM `attribute` WHERE {"`attr_id` = " + str(attr_id) if attr_id is not None else ""}{" AND " if attr_id is not None and attr_name is not None else ""}{"`attr_name` = '" + attr_name + "'" if attr_name is not None else ""}"""
        query_result = DB.execute_query(query, order=order, order_by=order_by, limit=limit)
        DB.disconnect()
        
        if query_result is None:
            return None
        
        if limit == 0 or limit > 1:
            result = []
            for i in query_result:
                result.append(Attribute(i[0], i[1]))
            return result
        elif limit == 1:
            return Attribute(query_result[0], query_result[1])
        else:
            return None
    
    def change_into(self, attr_id=None):
        if attr_id is None:
            self.attr_id = None
            self.attr_name = None
            return self
    
        DB.connect()
        query = f"SELECT * FROM `attribute` WHERE `attr_id` = {str(attr_id)}"
        query_result = DB.execute_query(query, limit=1)
        DB.disconnect()
        
        if query_result is None:
            return None
        
        self.attr_id = query_result[0]
        self.attr_name = query_result[1]
        
        return self

    def create(self, attr_name):
        DB.connect()
        query = f"INSERT INTO `attribute`(`attr_name`) VALUES ('{attr_name}')"
        query_result = DB.execute_query(query, limit=-1)
        DB.disconnect()
        
        if query_result is None:
            return None

        return self.change_into(query_result)
        
                
    def update(self, attr_name, attr_id=None):
        if attr_id is not None or self.attr_id is not None:
            DB.connect()
            query = f"UPDATE `attribute` SET `attr_name`= '{attr_name}' WHERE `attr_id` = {str(attr_id) if attr_id is not None else str(self.attr_id)}"
            query_result = DB.execute_query(query)
            DB.disconnect()
            
            if query_result is None:
                return None
            
            return self.change_into(attr_id=attr_id if attr_id is not None else self.attr_id)
        
    def delete(self, attr_id=None):
        if attr_id is not None or self.attr_id is not None:
            DB.connect()
            query = f"DELETE FROM `attribute` WHERE `attr_id` = {str(attr_id) if attr_id is not None else str(self.attr_id)}"
            query_result = DB.execute_query(query)
            DB.disconnect()
            
            if query_result is None:
                return None
            
            return self.change_into()
            