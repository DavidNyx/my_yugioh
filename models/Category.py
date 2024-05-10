import sys
sys.path.append('./')
from models.Database import DB
class Category:
    def __init__(self, category_id:int=None, category_name:str=None):
        self.category_id = category_id
        self.category_name = category_name
        
    def all(self):
        result = []
        DB.connect()
        query = "SELECT * FROM `category`"
        query_result = DB.execute_query(query)
        DB.disconnect()

        for i in query_result:
            result.append(Category(i[0], i[1]))
        
        return result

    def filter(self, category_id=None, category_name=None, first=False):
        if category_id is None and category_name is None:
            return all()
        
        result = []
        DB.connect()
        query = f"""SELECT * FROM `category` WHERE {"`category_id` = '" + category_id + "'" if category_id is not None else ""} {" AND " if username is not None and created_at is not None else ""} {"`created_at` = '" + created_at + "'" if created_at is not None else ""} {" LIMIT 1" if first == True else ""}"""
        query_result = DB.execute_query(query)
        DB.disconnect()
        
        for i in query_result:
            result.append(Category(i[0], i[1]))
        
        if first == True:
            return result[0]
        return result
    
    def change_into(self, category_id):
        DB.connect()
        query = f"SELECT * FROM `category` WHERE `category_id` = '{category_id}'"
        query_result = DB.execute_query(query)
        DB.disconnect()
        
        self.category_id = query_result[0][0]
        self.category_name = query_result[0][1]
        
        return self

    def create(self, category_name):
        DB.connect()
        query = f"INSERT INTO `category`(`category_name`) VALUES ('{category_name}')"
        query_result = DB.execute_query(query)
        DB.disconnect()
        
        if query_result == False:
            return None

        return self.change_into(query_result)
        
                
    def update(self, category_name, category_id=None):
        if category_id is not None or self.category_id is not None:
            DB.connect()
            query = f"UPDATE `category` SET `category_name`= '{category_name}' WHERE `category_id` = '{category_id if category_id is not None else self.category_id}'"
            query_result = DB.execute_query(query)
            DB.disconnect()
            
            if query_result == False:
                return None
            
            return self.change_into(category_id=category_id if category_id is not None else self.category_id)
        
    def delete(self, category_id=None):
        if category_id is not None or self.category_id is not None:
            DB.connect()
            query = f"DELETE FROM `category` WHERE `category_id` = '{category_id if category_id is not None else self.category_id}'"
            query_result = DB.execute_query(query)
            DB.disconnect()
            
            return None
            