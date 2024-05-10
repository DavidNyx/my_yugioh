import datetime
import bcrypt
import sys
sys.path.append('./')
from models.Database import DB

class User:
    def __init__(self, username:str=None, password:str=None, created_at:datetime.datetime=None):
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
            result.append(User(i[0], i[1], i[2]))
        
        return result

    def filter(self, username=None, created_at=None, first=False):
        if username is None and created_at is None:
            return all()
        
        result = []
        DB.connect()
        query = f"""SELECT * FROM `user` WHERE {"`username` = '" + username + "'" if username is not None else ""} {" AND " if username is not None and created_at is not None else ""} {"`created_at` = '" + created_at + "'" if created_at is not None else ""} {" LIMIT 1" if first == True else ""}"""
        query_result = DB.execute_query(query)
        DB.disconnect()
        
        for i in query_result:
            result.append(User(i[0], i[1], i[2]))
        
        if first == True:
            return result[0]
        return result
    
    def change_into(self, username):
        DB.connect()
        query = f"SELECT * FROM `user` WHERE `username` = '{username}'"
        query_result = DB.execute_query(query)
        DB.disconnect()
        
        self.username = query_result[0][0]
        self.password = query_result[0][1]
        self.created_at = query_result[0][2]
        
        return self

    def create(self, username, password):
        DB.connect()
        query = f"INSERT INTO `user`(`username`, `password`) VALUES ('{username}','{self.hash_password(password).decode('utf-8')}')"
        query_result = DB.execute_query(query)
        DB.disconnect()
        
        if query_result == False:
            return None

        return self.change_into(username)
        
                
    def update(self, password, username=None):
        if username is not None or self.username is not None:
            DB.connect()
            query = f"UPDATE `user` SET `password`= '{self.hash_password(password).decode('utf-8')}' WHERE `username` = '{username if username is not None else self.username}'"
            query_result = DB.execute_query(query)
            DB.disconnect()
            
            if query_result == False:
                return None
            
            return self.change_into(username=username if username is not None else self.username)
        
    def delete(self, username=None):
        if username is not None or self.username is not None:
            DB.connect()
            query = f"DELETE FROM `user` WHERE `username` = '{username if username is not None else self.username}'"
            query_result = DB.execute_query(query)
            DB.disconnect()
            
            return None
            