import sys
sys.path.append('./')
from models.Database import DB

class LinkArrow:
    def __init__(self, link_arrow_id:int=None, link_arrow_name:str=None):
        self.link_arrow_id = link_arrow_id
        self.link_arrow_name = link_arrow_name
        
    def all(self):
        result = []
        DB.connect()
        query = "SELECT * FROM `link_arrow`"
        query_result = DB.execute_query(query)
        DB.disconnect()

        for i in query_result:
            result.append(LinkArrow(i[0], i[1]))
        
        return result

    def filter(self, link_arrow_id=None, link_arrow_name=None, first=False):
        if link_arrow_id is None and link_arrow_name is None:
            return all()
        
        result = []
        DB.connect()
        query = f"""SELECT * FROM `link_arrow` WHERE {"`link_arrow_id` = " + str(link_arrow_id) if link_arrow_id is not None else ""} {" AND " if link_arrow_id is not None and link_arrow_name is not None else ""} {"`link_arrow_name` = '" + link_arrow_name + "'" if link_arrow_name is not None else ""} {" LIMIT 1" if first == True else ""}"""
        query_result = DB.execute_query(query)
        DB.disconnect()
        
        for i in query_result:
            result.append(LinkArrow(i[0], i[1]))
        
        if first == True:
            return result[0]
        return result
    
    def change_into(self, link_arrow_id):
        DB.connect()
        query = f"SELECT * FROM `link_arrow` WHERE `link_arrow_id` = {str(link_arrow_id)}"
        query_result = DB.execute_query(query)
        DB.disconnect()
        
        self.link_arrow_id = query_result[0][0]
        self.link_arrow_name = query_result[0][1]
        
        return self

    def create(self, link_arrow_name):
        DB.connect()
        query = f"INSERT INTO `link_arrow`(`link_arrow_name`) VALUES ('{link_arrow_name}')"
        query_result = DB.execute_query(query)
        DB.disconnect()
        
        if query_result == False:
            return None

        return self.change_into(query_result)
        
                
    def update(self, link_arrow_name, link_arrow_id=None):
        if link_arrow_id is not None or self.link_arrow_id is not None:
            DB.connect()
            query = f"UPDATE `link_arrow` SET `link_arrow_name`= '{link_arrow_name}' WHERE `link_arrow_id` = {str(link_arrow_id) if link_arrow_id is not None else str(self.link_arrow_id)}"
            query_result = DB.execute_query(query)
            DB.disconnect()
            
            if query_result == False:
                return None
            
            return self.change_into(link_arrow_id=link_arrow_id if link_arrow_id is not None else self.link_arrow_id)
        
    def delete(self, link_arrow_id=None):
        if link_arrow_id is not None or self.link_arrow_id is not None:
            DB.connect()
            query = f"DELETE FROM `link_arrow` WHERE `link_arrow_id` = {str(link_arrow_id) if link_arrow_id is not None else str(self.link_arrow_id)}"
            query_result = DB.execute_query(query)
            DB.disconnect()
            
            return None
            