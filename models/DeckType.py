import sys
import importlib
sys.path.append('./')
from models.Database import DB
try:
    Card_Deck = importlib.import_module("Card_Deck")
except:
    Card_Deck = importlib.import_module("models.Card_Deck")

class DeckType:
    def __init__(self, deck_type_id:int=None, deck_type_name:str=None, min_size:int=None, max_size:int=None, card_decks:list=[]):
        self.deck_type_id = deck_type_id
        self.deck_type_name = deck_type_name
        self.min_size = min_size
        self.max_size = max_size
        self.card_decks = card_decks
        
    def all(self, order='deck_type_name', order_by='ASC', limit=0):
        DB.connect()
        query = "SELECT * FROM `deck_type`"
        query_result = DB.execute_query(query, order=order, order_by=order_by,limit=limit)
        DB.disconnect()
        
        if query_result is None:
            return None

        if limit == 0 or limit > 1:
            result = []
            for i in query_result:
                result.append(DeckType(i[0], i[1], i[2], i[3], Card_Deck.Card_Deck().filter(card_id=i[0], empty='deck_type')))
            return result
        elif limit == 1:
            return DeckType(query_result[0], query_result[1], query_result[2], query_result[3], Card_Deck.Card_Deck().filter(deck_type_id=query_result[0], empty='deck_type'))
        else:
            return None

    def filter(self, deck_type_id=None, deck_type_name=None, min_size=None, max_size=None, order='deck_type_name', order_by='ASC', limit=0):
        if deck_type_id is None and deck_type_name is None and min_size is None and max_size is None:
            return DeckType().all()
        
        DB.connect()
        query = f"""SELECT * FROM `deck_type` WHERE {"`deck_type_id` = " + str(deck_type_id) if deck_type_id is not None else ""}{" AND " if deck_type_id is not None and deck_type_name is not None else ""}{"`deck_type_name` = '" + deck_type_name + "'" if deck_type_name is not None else ""}{" AND " if (deck_type_id is not None or deck_type_name is not None) and min_size is not None else ""}{"min_size = " + str(min_size) if min_size is not None else ""}{" AND " if (deck_type_id is not None or deck_type_name is not None or min_size is not None) and max_size is not None else ""}{"max_size = " + str(max_size) if max_size is not None else ""}"""
        query_result = DB.execute_query(query, order=order, order_by=order_by,limit=limit)
        DB.disconnect()
        
        if query_result is None:
            return None
        
        if limit == 0 or limit > 1:
            result = []
            for i in query_result:
                result.append(DeckType(i[0], i[1], i[2], i[3], Card_Deck.Card_Deck().filter(deck_type_id=i[0], empty='deck_type')))
            return result
        elif limit == 1:
            return DeckType(query_result[0], query_result[1], query_result[2], query_result[3], Card_Deck.Card_Deck().filter(deck_type_id=query_result[0], empty='deck_type'))
        else:
            return None
        
    def change_into(self, deck_type_id=None, empty=None):
        if deck_type_id is None:
            self.deck_type_id = None
            self.deck_type_name = None
            self.min_size = None
            self.max_size = None
            self.card_decks = []
            return self
        
        DB.connect()
        query = f"SELECT * FROM `deck_type` WHERE `deck_type_id` = {str(deck_type_id)}"
        query_result = DB.execute_query(query, limit=1)
        DB.disconnect()
        
        if query_result is None:
            return None
        
        self.deck_type_id = query_result[0]
        self.deck_type_name = query_result[1]
        self.min_size = query_result[2]
        self.max_size = query_result[3]
        if empty != 'card' or empty != 'deck':
            self.card_decks = Card_Deck.Card_Deck().filter(deck_type_id=query_result[0], empty='deck_type')
        else:
            self.card_decks = []
        
        return self

    def create(self, deck_type_name, min_size, max_size):
        DB.connect()
        query = f"INSERT INTO `deck_type`(`deck_type_name`, `min_size`, `max_size`) VALUES ('{deck_type_name}', {str(min_size)}, {str(max_size)})"
        query_result = DB.execute_query(query, limit=-1)
        DB.disconnect()
        
        if query_result is None:
            return None

        return self.change_into(query_result)
        
                
    def update(self, deck_type_id=None, deck_type_name=None, min_size=None, max_size=None):
        if deck_type_id is not None or self.deck_type_id is not None:
            DB.connect()
            query = f"""UPDATE `deck_type` SET {"`deck_type_name`= '" + deck_type_name + "'" if deck_type_name is not None else ""}{", " if deck_type_name is not None and min_size is not None else ""}{"`min_size` = " + str(min_size) if min_size is not None else ""}{", " if (deck_type_name is not None or min_size is not None) and max_size is not None else ""}{"`max_size` = " + str(max_size) if max_size is not None else ""} WHERE `deck_type_id` = {str(deck_type_id) if deck_type_id is not None else str(self.deck_type_id)}"""
            query_result = DB.execute_query(query)
            DB.disconnect()
            
            if query_result is None:
                return None
            
            return self.change_into(deck_type_id=deck_type_id if deck_type_id is not None else self.deck_type_id)
        
    def delete(self, deck_type_id=None):
        if deck_type_id is not None or self.deck_type_id is not None:
            Card_Deck.Card_Deck().delete(deck_type_id=deck_type_id if deck_type_id is not None else self.deck_type_id)
            DB.connect()
            query = f"DELETE FROM `deck_type` WHERE `deck_type_id` = {str(deck_type_id) if deck_type_id is not None else str(self.deck_type_id)}"
            query_result = DB.execute_query(query)
            DB.disconnect()
            
            if query_result is None:
                return None
            
            return self.change_into()
            