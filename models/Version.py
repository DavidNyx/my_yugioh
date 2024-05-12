import sys
sys.path.append('./')
from models.Database import DB

class Version:
    def __init__(self, version_id:int=None, version_name:str=None):
        self.version_id = version_id
        self.version_name = version_name
        
    def all(self):
        result = []
        DB.connect()
        query = "SELECT * FROM `version`"
        query_result = DB.execute_query(query)
        DB.disconnect()

        for i in query_result:
            result.append(Version(i[0], i[1]))
        
        return result

    def filter(self, version_id=None, version_name=None, first=False):
        if version_id is None and version_name is None:
            return all()
        
        result = []
        DB.connect()
        query = f"""SELECT * FROM `version` WHERE {"`version_id` = " + str(version_id) if version_id is not None else ""} {" AND " if version_id is not None and version_name is not None else ""} {"`version_name` = '" + version_name + "'" if version_name is not None else ""} {" LIMIT 1" if first == True else ""}"""
        query_result = DB.execute_query(query)
        DB.disconnect()
        
        for i in query_result:
            result.append(Version(i[0], i[1]))
        
        if first == True:
            return result[0]
        return result
    
    def change_into(self, version_id):
        DB.connect()
        query = f"SELECT * FROM `version` WHERE `version_id` = {str(version_id)}"
        query_result = DB.execute_query(query)
        DB.disconnect()
        
        self.version_id = query_result[0][0]
        self.version_name = query_result[0][1]
        
        return self

    def create(self, version_name):
        DB.connect()
        query = f"INSERT INTO `version`(`version_name`) VALUES ('{version_name}')"
        query_result = DB.execute_query(query)
        DB.disconnect()
        
        if query_result == False:
            return None

        return self.change_into(query_result)
        
                
    def update(self, version_name, version_id=None):
        if version_id is not None or self.version_id is not None:
            DB.connect()
            query = f"UPDATE `version` SET `version_name`= '{version_name}' WHERE `version_id` = {str(version_id) if version_id is not None else str(self.version_id)}"
            query_result = DB.execute_query(query)
            DB.disconnect()
            
            if query_result == False:
                return None
            
            return self.change_into(version_id=version_id if version_id is not None else self.version_id)
        
    def delete(self, version_id=None):
        if version_id is not None or self.version_id is not None:
            DB.connect()
            query = f"DELETE FROM `version` WHERE `version_id` = {str(version_id) if version_id is not None else str(self.version_id)}"
            query_result = DB.execute_query(query)
            DB.disconnect()
            
            return None
            