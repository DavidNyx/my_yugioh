import sys
import importlib
sys.path.append('./')
from models.Database import DB
try:
    Card_Version = importlib.import_module("Card_Version")
except:
    Card_Version = importlib.import_module("models.Card_Version")

class Version:
    def __init__(self, version_id:int=None, version_name:str=None, card_versions:list=[]):
        self.version_id = version_id
        self.version_name = version_name
        self.card_versions = card_versions
        
    def all(self, order='version_name', order_by='ASC', limit=0):
        DB.connect()
        query = "SELECT * FROM `version`"
        query_result = DB.execute_query(query, order=order, order_by=order_by, limit=limit)
        DB.disconnect()
        
        if query_result is None:
            return None

        if limit == 0 or limit > 1:
            result = []
            for i in query_result:
                result.append(Version(i[0], i[1], Card_Version.Card_Version().filter(version_id=i[0], empty='version')))
            return result
        elif limit == 1:
            return Version(query_result[0], query_result[1], Card_Version.Card_Version().filter(version_id=query_result[0], empty='version'))
        else:
            return None

    def filter(self, version_id=None, version_name=None, order='version_name', order_by='ASC', limit=0):
        if version_id is None and version_name is None:
            return Version().all()
        
        DB.connect()
        query = f"""SELECT * FROM `version` WHERE {"`version_id` = " + str(version_id) if version_id is not None else ""}{" AND " if version_id is not None and version_name is not None else ""}{"`version_name` = '" + version_name + "'" if version_name is not None else ""}"""
        query_result = DB.execute_query(query, order=order, order_by=order_by, limit=limit)
        DB.disconnect()
        
        if query_result is None:
            return None
        
        if limit == 0 or limit > 1:
            result = []
            for i in query_result:
                result.append(Version(i[0], i[1], Card_Version.Card_Version().filter(version_id=i[0], empty='version')))
            return result
        elif limit == 1:
            return Version(query_result[0], query_result[1], Card_Version.Card_Version().filter(version_id=query_result[0], empty='version'))
        else:
            return None
    
    def change_into(self, version_id=None):
        if version_id is None:
            self.version_id = None
            self.version_name = None
            self.card_versions = []
            return self
        DB.connect()
        query = f"SELECT * FROM `version` WHERE `version_id` = {str(version_id)}"
        query_result = DB.execute_query(query, limit=1)
        DB.disconnect()
        
        if query_result is None:
            return None
        
        self.version_id = query_result[0]
        self.version_name = query_result[1]
        self.card_versions = Card_Version.Card_Version().filter(version_id=query_result[0], empty='version')
        
        return self

    def create(self, version_name):
        DB.connect()
        query = f"INSERT INTO `version`(`version_name`) VALUES ('{version_name}')"
        query_result = DB.execute_query(query, limit=-1)
        DB.disconnect()
        
        if query_result is None:
            return None

        return self.change_into(query_result)
        
                
    def update(self, version_name, version_id=None):
        if version_id is not None or self.version_id is not None:
            DB.connect()
            query = f"UPDATE `version` SET `version_name`= '{version_name}' WHERE `version_id` = {str(version_id) if version_id is not None else str(self.version_id)}"
            query_result = DB.execute_query(query)
            DB.disconnect()
            
            if query_result is None:
                return None
            
            return self.change_into(version_id=version_id if version_id is not None else self.version_id)
        
    def delete(self, version_id=None):
        if version_id is not None or self.version_id is not None:
            Card_Version.Card_Version().delete(version_id=version_id if version_id is not None else self.version_id) 
            DB.connect()
            query = f"DELETE FROM `version` WHERE `version_id` = {str(version_id) if version_id is not None else str(self.version_id)}"
            query_result = DB.execute_query(query)
            DB.disconnect()
            
            if query_result is None:
                return None
            
            return self.change_into()
            