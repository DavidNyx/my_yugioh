import sys
sys.path.append('./')
from models.Database import DB

class Category:
    def __init__(self, category_id:int=None, category_name:str=None):
        self.category_id = category_id
        self.category_name = category_name
        
    def all(self, order='category_name', order_by='ASC', limit=0):
        DB.connect()
        query = "SELECT * FROM `category`"
        query_result = DB.execute_query(query, order=order, order_by=order_by, limit=limit)
        DB.disconnect()

        if limit == 0 or limit > 1:
            result = []
            for i in query_result:
                result.append(Category(i[0], i[1]))
            return result
        elif limit == 1:
            return Category(query_result[0], query_result[1])
        else:
            return None

    def filter(self, category_id=None, category_name=None, order='category_name', order_by='ASC', limit=0):
        if category_id is None and category_name is None:
            return all()
        
        DB.connect()
        query = f"""SELECT * FROM `category` WHERE {"`category_id` = " + str(category_id) if category_id is not None else ""}{" AND " if category_id is not None and category_name is not None else ""}{"`category_name` = '" + category_name + "'" if category_name is not None else ""}"""
        query_result = DB.execute_query(query, order=order, order_by=order_by, limit=limit)
        DB.disconnect()
        
        if limit == 0 or limit > 1:
            result = []
            for i in query_result:
                result.append(Category(i[0], i[1]))
            return result
        elif limit == 1:
            return Category(query_result[0], query_result[1])
        else:
            return None
    
    def change_into(self, category_id=None):
        if category_id is None:
            self.category_id = None
            self.category_name = None
            return self
        
        DB.connect()
        query = f"SELECT * FROM `category` WHERE `category_id` = {str(category_id)}"
        query_result = DB.execute_query(query, limit=1)
        DB.disconnect()
        
        self.category_id = query_result[0]
        self.category_name = query_result[1]
        
        return self

    def create(self, category_name):
        DB.connect()
        query = f"INSERT INTO `category`(`category_name`) VALUES ('{category_name}')"
        query_result = DB.execute_query(query, limit=-1)
        DB.disconnect()
        
        if query_result == False:
            return None

        return self.change_into(query_result)
        
                
    def update(self, category_name, category_id=None):
        if category_id is not None or self.category_id is not None:
            DB.connect()
            query = f"UPDATE `category` SET `category_name`= '{category_name}' WHERE `category_id` = {str(category_id) if category_id is not None else str(self.category_id)}"
            query_result = DB.execute_query(query)
            DB.disconnect()
            
            if query_result == False:
                return None
            
            return self.change_into(category_id=category_id if category_id is not None else self.category_id)
        
    def delete(self, category_id=None):
        if category_id is not None or self.category_id is not None:
            DB.connect()
            query = f"DELETE FROM `category` WHERE `category_id` = {str(category_id) if category_id is not None else str(self.category_id)}"
            query_result = DB.execute_query(query)
            DB.disconnect()
            
            return self.change_into()
            