import sys
sys.path.append('./')
from models.Database import DB

class SubCategory:
    def __init__(self, subcategory_id:int=None, subcategory_name:str=None):
        self.subcategory_id = subcategory_id
        self.subcategory_name = subcategory_name
        
    def all(self):
        result = []
        DB.connect()
        query = "SELECT * FROM `subcategory`"
        query_result = DB.execute_query(query)
        DB.disconnect()

        for i in query_result:
            result.append(SubCategory(i[0], i[1]))
        
        return result

    def filter(self, subcategory_id=None, subcategory_name=None, first=False):
        if subcategory_id is None and subcategory_name is None:
            return all()
        
        result = []
        DB.connect()
        query = f"""SELECT * FROM `subcategory` WHERE {"`subcategory_id` = " + str(subcategory_id) if subcategory_id is not None else ""} {" AND " if subcategory_id is not None and subcategory_name is not None else ""} {"`subcategory_name` = '" + subcategory_name + "'" if subcategory_name is not None else ""} {" LIMIT 1" if first == True else ""}"""
        query_result = DB.execute_query(query)
        DB.disconnect()
        
        for i in query_result:
            result.append(SubCategory(i[0], i[1]))
        
        if first == True:
            return result[0]
        return result
    
    def change_into(self, subcategory_id):
        DB.connect()
        query = f"SELECT * FROM `subcategory` WHERE `subcategory_id` = {str(subcategory_id)}"
        query_result = DB.execute_query(query)
        DB.disconnect()
        
        self.subcategory_id = query_result[0][0]
        self.subcategory_name = query_result[0][1]
        
        return self

    def create(self, subcategory_name):
        DB.connect()
        query = f"INSERT INTO `subcategory`(`subcategory_name`) VALUES ('{subcategory_name}')"
        query_result = DB.execute_query(query)
        DB.disconnect()
        
        if query_result == False:
            return None

        return self.change_into(query_result)
        
                
    def update(self, subcategory_name, subcategory_id=None):
        if subcategory_id is not None or self.subcategory_id is not None:
            DB.connect()
            query = f"UPDATE `subcategory` SET `subcategory_name`= '{subcategory_name}' WHERE `subcategory_id` = {str(subcategory_id) if subcategory_id is not None else str(self.subcategory_id)}"
            query_result = DB.execute_query(query)
            DB.disconnect()
            
            if query_result == False:
                return None
            
            return self.change_into(subcategory_id=subcategory_id if subcategory_id is not None else self.subcategory_id)
        
    def delete(self, subcategory_id=None):
        if subcategory_id is not None or self.subcategory_id is not None:
            DB.connect()
            query = f"DELETE FROM `subcategory` WHERE `subcategory_id` = {str(subcategory_id) if subcategory_id is not None else str(self.subcategory_id)}"
            query_result = DB.execute_query(query)
            DB.disconnect()
            
            return None
            