import sys
import importlib
sys.path.append('./')
from models.Database import DB
try:
    Card_SubCategory = importlib.import_module("Card_SubCategory")
except:
    Card_SubCategory = importlib.import_module("models.Card_SubCategory")
class SubCategory:
    def __init__(self, subcategory_id:int=None, subcategory_name:str=None, card_subcategories:list=[]):
        self.subcategory_id = subcategory_id
        self.subcategory_name = subcategory_name
        self.card_subcategories = card_subcategories
        
    def all(self, order='subcategory_name', order_by='ASC', limit=0):
        DB.connect()
        query = "SELECT * FROM `subcategory`"
        query_result = DB.execute_query(query, order=order, order_by=order_by, limit=limit)
        DB.disconnect()
        
        if query_result is None:
            return None

        if limit == 0 or limit > 1:
            result = []
            for i in query_result:
                result.append(SubCategory(i[0], i[1], Card_SubCategory.Card_SubCategory().filter(subcategory_id=i[0], empty='subcategory')))
            return result
        elif limit == 1:
            return SubCategory(query_result[0], query_result[1], Card_SubCategory.Card_SubCategory().filter(subcategory_id=query_result[0], empty='subcategory'))
        else:
            return None

    def filter(self, subcategory_id=None, subcategory_name=None, order='subcategory_name', order_by='ASC', limit=0):
        if subcategory_id is None and subcategory_name is None:
            return SubCategory().all()
        
        DB.connect()
        query = f"""SELECT * FROM `subcategory` WHERE {"`subcategory_id` = " + str(subcategory_id) if subcategory_id is not None else ""}{" AND " if subcategory_id is not None and subcategory_name is not None else ""}{"`subcategory_name` = '" + subcategory_name + "'" if subcategory_name is not None else ""}"""
        query_result = DB.execute_query(query, order=order, order_by=order_by, limit=limit)
        DB.disconnect()
        
        if query_result is None:
            return None
        
        if limit == 0 or limit > 1:
            result = []
            for i in query_result:
                result.append(SubCategory(i[0], i[1], Card_SubCategory.Card_SubCategory().filter(subcategory_id=i[0], empty='subcategory')))
            return result
        elif limit == 1:
            return SubCategory(query_result[0], query_result[1], Card_SubCategory.Card_SubCategory().filter(subcategory_id=query_result[0], empty='subcategory'))
        else:
            return None
    
    def change_into(self, subcategory_id=None, empty=None):
        if subcategory_id is None:
            self.subcategory_id = None
            self.subcategory_name = None
            self.card_subcategories = []
            return self
        DB.connect()
        query = f"SELECT * FROM `subcategory` WHERE `subcategory_id` = {str(subcategory_id)}"
        query_result = DB.execute_query(query, limit=1)
        DB.disconnect()
        
        if query_result is None:
            return None
        
        self.subcategory_id = query_result[0]
        self.subcategory_name = query_result[1]
        if empty != 'card':
            self.card_subcategories = Card_SubCategory.Card_SubCategory().filter(subcategory_id=query_result[0], empty='subcategory')
        else:
            self.card_subcategories = []
        return self

    def create(self, subcategory_name):
        DB.connect()
        query = f"INSERT INTO `subcategory`(`subcategory_name`) VALUES ('{subcategory_name}')"
        query_result = DB.execute_query(query, limit=-1)
        DB.disconnect()
        
        if query_result is None:
            return None

        return self.change_into(query_result)
        
                
    def update(self, subcategory_name, subcategory_id=None):
        if subcategory_id is not None or self.subcategory_id is not None:
            DB.connect()
            query = f"UPDATE `subcategory` SET `subcategory_name`= '{subcategory_name}' WHERE `subcategory_id` = {str(subcategory_id) if subcategory_id is not None else str(self.subcategory_id)}"
            query_result = DB.execute_query(query)
            DB.disconnect()
            
            if query_result is None:
                return None
            
            return self.change_into(subcategory_id=subcategory_id if subcategory_id is not None else self.subcategory_id)
        
    def delete(self, subcategory_id=None):
        if subcategory_id is not None or self.subcategory_id is not None:
            Card_SubCategory.Card_SubCategory().delete(subcategory_id=subcategory_id if subcategory_id is not None else self.subcategory_id)
            DB.connect()
            query = f"DELETE FROM `subcategory` WHERE `subcategory_id` = {str(subcategory_id) if subcategory_id is not None else str(self.subcategory_id)}"
            query_result = DB.execute_query(query)
            DB.disconnect()
            
            if query_result is None:
                return None
            
            return self.change_into()
            