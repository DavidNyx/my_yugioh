import datetime
import sys
sys.path.append('./')
from models.User import User
from models.Database import DB

class Deck:
    def __init__(self, deck_id:int=None, deck_name:str=None, owner_id:str=None, created_at:datetime.datetime=None, updated_at:datetime.datetime=None):
        self.deck_id = deck_id
        self.deck_name = deck_name
        self.owner = User.change_into(user_id=owner_id)
        self.created_at = created_at
        self.updated_at = updated_at
        
    def all(self, order='deck_name', order_by='ASC', limit=0):
        DB.connect()
        query = "SELECT * FROM `deck`"
        query_result = DB.execute_query(query, order=order, order_by=order_by, limit=limit)
        DB.disconnect()
        
        if query_result is None:
            return None

        if limit == 0 or limit > 1:
            result = []
            for i in query_result:
                result.append(Deck(i[0], i[1], i[2], i[3], i[4]))
            return result
        elif limit == 1:
            return Deck(query_result[0], query_result[1], query_result[2], query_result[3], query_result[4])
        else:
            return None

    def filter(self, deck_id=None, deck_name=None, owner_id=None, created_at=None, updated_at=None, limit=0, order='deck_id', order_by='ASC'):
        if deck_id is None and deck_name and owner_id is None and created_at is None and updated_at is None:
            return all()
        
        DB.connect()
        query = f"""SELECT * FROM `deck` WHERE {"`deck_id` = " + str(deck_id) if deck_id is not None else ""}{" AND " if deck_id is not None and deck_name is not None else ""}{"`deck_name` LIKE '%" + deck_name + "%'" if deck_name is not None else ""}{" AND " if (deck_id is not None or deck_name is not None) and owner_id is not None else ""}{"`owner_id` = " + str(owner_id) if owner_id is not None else ""}{" AND " if (deck_id is not None or deck_name is not None or owner_id is not None) and created_at is not None else ""}{"`created_at` = '" + created_at + "'" if created_at is not None else ""}{" AND " if (deck_id is not None or deck_name is not None or owner_id is not None or created_at is not None) and updated_at is not None else ""}{"updated_at = '" + updated_at + "'" if updated_at is not None else ""}"""
        query_result = DB.execute_query(query, order=order, order_by=order_by, limit=limit)
        DB.disconnect()
        
        if query_result is None:
            return None
        
        if limit == 0 or limit > 1:
            result = []
            for i in query_result:
                result.append(Deck(i[0], i[1], i[2], i[3], i[4]))
            return result
        elif limit == 1:
            return Deck(query_result[0], query_result[1], query_result[2], query_result[3], query_result[4])
        else:
            return None
    
    def change_into(self, deck_id=None):
        if deck_id is None:
            self.deck_id = None
            self.deck_name = None
            self.owner = None
            self.created_at = None
            self.updated_at = None
            return self
        
        DB.connect()
        query = f"SELECT * FROM `deck` WHERE `deck_id` = {str(deck_id)}"
        query_result = DB.execute_query(query, limit=1)
        DB.disconnect()
        
        if query_result is None:
            return None
        
        self.deck_id = query_result[0]
        self.deck_name = query_result[1]
        self.owner = User().change_into(query_result[2])
        self.created_at = query_result[3]
        self.updated_at = query_result[4]
        
        return self

    def create(self, deck_name, owner_id):
        DB.connect()
        query = f"INSERT INTO `deck`(`deck_name`, `owner_id`) VALUES ('{deck_name}', {str(owner_id)})"
        query_result = DB.execute_query(query, limit=-1)
        DB.disconnect()
        
        if query_result is None:
            return None
        
        return self.change_into(query_result)

    def update(self, deck_id=None, deck_name=None, owner_id=None):
        if (owner_id is None and deck_name is None) or (deck_id is None and self.deck_id is None):
            return self
        
        DB.connect()
        query = f"""UPDATE `deck` SET {"`deck_name` = '" + deck_name + "'" if deck_name is not None else ""}{", " if deck_name is not None and owner_id is not None else ""}{"`owner_id` = " + str(owner_id) if owner_id is not None else ""}, `updated_at` = '{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}' WHERE `deck_id` = {str(deck_id) if deck_id is not None else str(self.deck_id)}"""
        query_result = DB.execute_query(query)
        DB.disconnect()
        
        if query_result is None:
            return None
        
        return self.change_into(deck_id=deck_id if deck_id is not None else self.deck_id)

    def delete(self, deck_id=None):
        if deck_id is not None or self.deck_id is not None:
            DB.connect()
            query = f"DELETE FROM `deck` WHERE `deck_id` = {str(deck_id) if deck_id is not None else str(self.deck_id)}"
            query_result = DB.execute_query(query)
            DB.disconnect()
            
            if query_result is None:
                return None

        return self.change_into()
    