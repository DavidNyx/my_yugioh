import sys
import importlib
sys.path.append('./')
from models.Database import DB
try:
    Card = importlib.import_module("Card")
except:
    Card = importlib.import_module("models.Card")
try:
    Deck = importlib.import_module("Deck")
except:
    Deck = importlib.import_module("models.Deck")
try:
    DeckType = importlib.import_module("DeckType")
except:
    DeckType = importlib.import_module("models.DeckType")

class Card_Deck():
    def __init__(self, card_id:str=None, deck_id:int=None, deck_type_id:int=None, number_of_copies:int=0):
        self.card = Card.Card().change_into(card_id=card_id)
        self.deck = Deck.Deck().change_into(deck_id=deck_id)
        self.deck_type = DeckType.DeckType().change_into(deck_type_id=deck_type_id)
        self.number_of_copies = number_of_copies
        
    def all(self, order='card_id', order_by='ASC', limit=0):
        DB.connect()
        query = f"SELECT * FROM `card_deck`"
        query_result = DB.execute_query(query, order=order, order_by=order_by, limit=limit)
        DB.disconnect()
        
        if query_result is None:
            return None
        
        if limit == 0 or limit > 1:
            result = []
            for i in query_result:
                result.append(Card_Deck(i[0], i[1], i[2], i[3]))
            return result
        elif limit == 1:
            return Card_Deck(query_result[0], query_result[1], query_result[2], query_result[3])
        else:
            return None
    
    def filter(self, card_id=None, deck_id=None, deck_type_id=None, order='card_id', order_by='ASC', limit=0, empty=None):
        if card_id is None and deck_id is None and deck_type_id is None:
            return all()
        
        DB.connect()
        query = f"""SELECT * FROM `card_deck` WHERE {"`card_id` = '" + card_id + "'" if card_id is not None else ""}{" AND " if card_id is not None and deck_id is not None else ""}{"`deck_id` = " + str(deck_id) if deck_id is not None else ""}{" AND " if (card_id is not None or deck_id is not None) and deck_type_id is not None else ""}"""
        query_result = DB.execute_query(query, order=order, order_by=order_by, limit=limit)
        DB.disconnect()
        
        if query_result is None:
            return None
        
        if limit == 0 or limit > 1:
            result = []
            for i in query_result:
                result.append(Card_Deck(i[0] if empty != 'card' else None, i[1] if empty != 'deck' else None, i[2] if empty != 'deck_type' else None, i[3]))
            return result
        elif limit == 1:
            return Card_Deck(query_result[0] if empty != 'card' else None, query_result[1] if empty != 'deck' else None, query_result[2] if empty != 'deck_type' else None, query_result[3])
        else:
            return None
        
    def change_into(self, card_id=None, deck_id=None, deck_type_id=None, number_of_copies=0):
        if card_id is None or deck_id is None or deck_type_id is None or number_of_copies == 0:
            self.card = None
            self.deck = None
            self.deck_type = None
            self.number_of_copies = 0
            return self
        
        DB.connect()
        query = f"""SELECT * FROM `card_deck` WHERE `card_id` = '{card_id}' AND `deck_id` = {str(deck_id)} AND `deck_type_id` = {str(deck_type_id)} AND `number_of_copies` = {str(number_of_copies)}"""
        query_result = DB.execute_query(query, limit=1)
        DB.disconnect()
        
        if query_result is None:
            return None
        
        self.card = Card.Card().change_into(card_id=query_result[0])
        self.deck = Deck.Deck().change_into(deck_id=query_result[1])
        self.deck_type = DeckType.DeckType().change_into(deck_type_id=query_result[2])
        self.number_of_copies = query_result[3]
        
        return self
    
    def create(self, card_id, deck_id, deck_type_id, number_of_copies):
        DB.connect()
        query = f"INSERT INTO `card_deck`(`card_id`, `deck_id`, `deck_type_id`, `number_of_copies`) VALUES ({card_id}, {str(deck_id)}, {str(deck_type_id)}, {str(number_of_copies)}"
        query_result = DB.execute_query(query)
        DB.disconnect()
        
        if query_result is None:
            return None
        
        return self.change_into(card_id=card_id, deck_id=deck_id, deck_type_id=deck_type_id, number_of_copies=number_of_copies)
    
    def update(self, card_id=None, deck_id=None, deck_type_id=None, number_of_copies=0):
        if ((card_id is None or deck_id is None or deck_type_id is None) and (self.card.card_id is None or self.deck.deck_id is None or self.deck_type.deck_type_id is None))  or number_of_copies == 0:
            return self
        
        DB.connect()
        query = f"""UPDATE `card_deck` SET `number_of_copies` = {str(number_of_copies)} WHERE `card_id` = '{card_id if card_id is not None else self.card.card_id}' AND `deck_id` = {str(deck_id) if deck_id is not None else str(self.deck.deck_id)} AND `deck_type_id` = {str(deck_type_id) if deck_type_id is not None else str(self.deck_type.deck_type_id)}"""
        query_result = DB.execute_query(query)
        DB.disconnect()
        
        if query_result is None:
            return None
        
        return self
        
    def delete(self, card_id=None, deck_id=None, deck_type_id=None):
        if card_id is not None or deck_id is not None or deck_type_id is not None:
            DB.connect()
            query = f"""DELETE FROM `card_deck` WHERE {"`card_id` = '" + card_id + "'" if card_id is not None else ""}{" AND " if card_id is not None and deck_id is not None else ""}{"`deck_id` = " + str(deck_id) if deck_id is not None else ""}{" AND " if (card_id is not None or deck_id is not None) and deck_type_id is not None else ""}{"`deck_type_id` = " + str(deck_type_id) if deck_type_id is not None else ""}"""
            query_result = DB.execute_query(query)
            DB.disconnect()
        elif self.card.card_id is not None and self.deck.deck_id is not None and self.deck_type.deck_type_id is not None:
            DB.connect()
            query = f"DELETE FROM `card_deck` WHERE `card_id` = '{self.card.card_id}' AND `deck_id` = {str(self.deck.deck_id)} AND `deck_type_id` = {str(self.deck_type.deck_type_id)}"
            query_result = DB.execute_query(query)
            DB.disconnect()
        
        if query_result is None:
            return None
        
        return self.change_into()