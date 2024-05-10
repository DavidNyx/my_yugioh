import sys
sys.path.append('./')
from models.Database import DB
from models.Category import Category

def all(selff):
    result = []
    DB.connect()
    query = "SELECT * FROM `category`"
    query_result = DB.execute_query(query)
    DB.disconnect()

    for i in query_result:
        result.append(Category(i[0], i[1]))
    
    return result

def filter(category_id=None, category_name=None, first=False, order_by='ASC'):
    if category_id is None and category_name is None:
        return all()
    
    result = []
    DB.connect()
    query = f"""SELECT * FROM `category` WHERE {'`category_id` = "' + category_id + '"' if category_id is not None else ''} {' AND ' if category_id is not None and category_name is not None else ''} {'`category_name` = "' + category_name + '"' if category_name is not None else ''} {' ORDER BY `deck_id` ' + order_by} {' LIMIT 1' if first == True else ''}"""
    query_result = DB.execute_query(query)
    DB.disconnect()
    
    for i in query_result:
        result.append(Category(i[0], i[1]))
        
    if first == True:
        return result[0]
    return result

def create(category_name):
    DB.connect()
    query = f"INSERT INTO `category`(`category_name`) VALUES ('{category_name}')"
    query_result = DB.execute_query(query)
    DB.disconnect()
    
    result = filter(category_name, first=True, order_by="DESC")
    return result

