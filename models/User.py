import datetime
import bcrypt
import sys
sys.path.append('./')
from models.Database import DB

class User:
    def __init__(self,user_id:int=None, username:str=None, password:str=None, created_at:datetime.datetime=None):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.created_at = created_at
    
    def hash_password(self, password):
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_password

    def verify_password(self, hashed_password, password):
        return bcrypt.checkpw(password.encode('utf-8'), hashed_password)

    def all(self):
        result = []
        DB.connect()
        query = "SELECT * FROM `user`"
        query_result = DB.execute_query(query)
        DB.disconnect()

        for i in query_result:
            result.append(User(i[0], i[1], i[2], i[3]))
        
        return result

    def filter(self, user_id=None, username=None, created_at=None, first=False):
        if user_id is None and username is None and created_at is None:
            return all()
        
        result = []
        DB.connect()
        query = f"""SELECT * FROM `user` WHERE {"`user_id` = " + str(user_id) if user_id is not None else ""} {" AND " if user_id is not None and username is not None else ""} {"`username` = '" + username + "'" if username is not None else ""} {" AND " if (user_id is not None or username is not None) and created_at is not None else ""} {"`created_at` = '" + created_at + "'" if created_at is not None else ""} {" LIMIT 1" if first == True else ""}"""
        query_result = DB.execute_query(query)
        DB.disconnect()
        
        for i in query_result:
            result.append(User(i[0], i[1], i[2], i[3]))
        
        if first == True:
            return result[0]
        return result
    
    def change_into(self, user_id):
        DB.connect()
        query = f"SELECT * FROM `user` WHERE `user_id` = {str(user_id)}"
        query_result = DB.execute_query(query)
        DB.disconnect()
        
        self.user_id = query_result[0][0]
        self.username = query_result[0][1]
        self.password = query_result[0][2]
        self.created_at = query_result[0][3]
        
        return self

    def create(self, username, password):
        DB.connect()
        query = f"INSERT INTO `user`(`username`, `password`) VALUES ('{username}','{self.hash_password(password).decode('utf-8')}')"
        query_result = DB.execute_query(query)
        DB.disconnect()
        
        if query_result == False:
            return None

        return self.change_into(query_result)
        
                
    def update(self, password=None, username=None, user_id=None):
        if (user_id is None and self.user_id is None) or (password is None and username is None):
            return self
        
        DB.connect()
        query = f"""UPDATE `user` SET {"`username` = '" + username + "'" if username is not None else ""} {", " if username is not None and password is not None else ""} {"`password` = '" + self.hash_password(password).decode('utf-8') + "'" if password is not None else ""} WHERE `user_id` = {str(user_id) if user_id is not None else str(self.user_id)}"""
        print(query)
        query_result = DB.execute_query(query)
        DB.disconnect()
        
        if query_result == False:
            return None
        
        return self.change_into(user_id=user_id if user_id is not None else self.user_id)
        
    def delete(self, user_id=None):
        if user_id is not None or self.user_id is not None:
            DB.connect()
            query = f"DELETE FROM `user` WHERE `user_id` = {str(user_id) if user_id is not None else str(self.user_id)}"
            query_result = DB.execute_query(query)
            DB.disconnect()
            
        return None
            