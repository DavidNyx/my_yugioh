import datetime
import sys
sys.path.append('./')
from models.User import User
from models.Database import DB

class Deck:
    def __init__(self, deck_id:int=None, owner:User=None, created_at:datetime.datetime=None, updated_at:datetime.datetime=None):
        self.deck_id = deck_id
        self.owner = owner
        self.created_at = created_at
        self.updated_at = updated_at
        
    def all(self):
        result = []
        DB.connect()
        query = "SELECT * FROM `deck`"
        query_result = DB.execute_query(query)
        DB.disconnect()

        for i in query_result:
            result.append(Deck(i[0], User.filter(username=i[1], first=True), i[2], i[3]))
        
        return result

    def filter(self, deck_id=None, owner_id=None, created_at=None, updated_at=None, first=False, order_by='ASC'):
        if deck_id is None and owner_id is None and created_at is None and updated_at is None:
            return all()
        
        result = []
        DB.connect()
        query = f"""SELECT * FROM `deck` WHERE {'`deck_id` = ' + str(deck_id) if deck_id is not None else ''} {' AND ' if deck_id is not None and owner_id is not None else ''} {'`owner_id` = "' + owner_id + '"' if owner_id is not None else ''} {' AND ' if (deck_id is not None or owner_id is not None) and created_at is not None else ''} {'`created_at` = "' + created_at + '"' if created_at is not None else ''} {' AND ' if (deck_id is not None or owner_id is not None or created_at is not None) and updated_at is not None else ''} {'`updated_at` = "' + updated_at + '"' if updated_at is not None else ''} {' ORDER BY `deck_id` ' + order_by} {' LIMIT 1' if first == True else ''}"""
        query_result = DB.execute_query(query)
        DB.disconnect()
        
        for i in query_result:
            result.append(Deck(i[0], User.change_into(username=i[1]), i[2], i[3]))
        
        if first == True:
            return result[0]
        return result
    
    def change_into(self, deck_id):
        DB.connect()
        query = f"SELECT * FROM `deck` WHERE `deck_id` = '{deck_id}'"
        query_result = DB.execute_query(query)
        DB.disconnect()
        
        self.deck_id = query_result[0][0]
        self.owner = User().change_into(query_result[0][1])
        self.created_at = query_result[0][2]
        self.updated_at = query_result[0][3]
        
        return self

    def create(self, owner_id):
        DB.connect()
        query = f"INSERT INTO `deck`(`owner_id`) VALUES ('{owner_id}')"
        query_result = DB.execute_query(query)
        DB.disconnect()
        
        if query_result == False:
            return None
        
        return self.change_into(deck_id=query_result)

    def update(self, deck_id=None, owner_id=None):
        if owner_id is None or (deck_id is None and self.deck_id is None):
            return self
        
        DB.connect()
        query = f"""UPDATE `deck` SET `owner_id` = '{owner_id}', `updated_at` = '{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}' WHERE `deck_id` = {str(deck_id) if deck_id is not None else str(self.deck_id)}"""
        print(query)
        query_result = DB.execute_query(query)
        DB.disconnect()
        
        if query_result == False:
            return None
        
        return self.change_into(deck_id=deck_id if deck_id is not None else self.deck_id)

    def delete(self, deck_id=None):
        if deck_id is not None or self.deck_id is not None:
            DB.connect()
            query = f"DELETE FROM `deck` WHERE `deck_id` = {str(deck_id) if deck_id is not None else str(self.deck_id)}"
            query_result = DB.execute_query(query)
            DB.disconnect() 

        return None
    