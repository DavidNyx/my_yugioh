import sys
import importlib
sys.path.append('./')
from models.Database import DB
from models.Category import Category
from models.CardType import CardType
from models.Attribute import Attribute
try:
    Card_Version = importlib.import_module("Card_Version")
except:
    Card_Version = importlib.import_module("models.Card_Version")
try:
    Card_Link = importlib.import_module("Card_Link")
except:
    Card_Link = importlib.import_module("models.Card_Link")
try:
    Card_SubCategory = importlib.import_module("Card_SubCategory")
except:
    Card_SubCategory = importlib.import_module("models.Card_SubCategory")
try:
    Card_Deck = importlib.import_module("Card_Deck")
except:
    Card_Deck = importlib.import_module("models.Card_Deck")
    
class Card:
    def __init__(self, card_id:str=None, card_name:str=None, desc:str=None, pendulum_effect:str=None, level_rank:int=None, scale:int=None, attack:int=None, defense:int=None, category_id:int=None, card_type_id:int=None, attr_id:int=None, card_versions:list=[], card_links:list=[], card_subcategories:list=[], card_decks:list=[]):
        self.card_id = card_id
        self.card_name = card_name
        self.desc = desc
        self.pendulum_effect = pendulum_effect
        self.level_rank = level_rank
        self.scale = scale
        self.attack = attack
        self.defense = defense
        self.category = Category().change_into(category_id=category_id)
        self.type = CardType().change_into(card_type_id=card_type_id)
        self.attr = Attribute().change_into(attr_id=attr_id)
        self.card_versions = card_versions
        self.card_links = card_links
        self.card_subcategories = card_subcategories
        self.card_decks = card_decks
        
    def all(self, order='card_name', order_by='ASC', limit=0):
        DB.connect()
        query = "SELECT * FROM `card`"
        query_result = DB.execute_query(query, order=order, order_by=order_by, limit=limit)
        DB.disconnect()
        
        if query_result is None:
            return None

        if limit == 0 or limit > 1:
            result = []
            for i in query_result:
                result.append(Card(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], Card_Version.Card_Version().filter(card_id=i[0], empty='card'), Card_Link.Card_Link().filter(card_id=i[0], empty='card'), Card_SubCategory.Card_SubCategory().filter(card_id=i[0], empty='card'), Card_Deck.Card_Deck().filter(card_id=i[0], empty='card')))
            return result
        elif limit == 1:
            return Card(query_result[0], query_result[1], query_result[2], query_result[3], query_result[4], query_result[5], query_result[6],query_result[7], query_result[8], query_result[9], query_result[10], Card_Version.Card_Version().filter(card_id=query_result[0], empty='card'), Card_Link.Card_Link().filter(card_id=query_result[0]), Card_SubCategory.Card_SubCategory().filter(card_id=query_result[0]), Card_Deck.Card_Deck().filter(card_id=query_result[0], empty='card'))
        else:
            return None
        
    def filter(self, card_id=None, card_name=None, desc=None, pendulum_effect=None, level_rank=None, scale=None, attack=None, defense=None, category_id=None, card_type_id=None, attr_id=None, order='card_name', order_by='ASC', limit=0):
        if card_id is None and card_name is None and desc is None and pendulum_effect is None and level_rank is None and scale is None and attack is None and defense is None and category_id is None and card_type_id is None and attr_id is None:
            return Card().all()
        
        
        DB.connect()
        query = f"""SELECT * FROM `card` WHERE {"card_id = '" + card_id + "'" if card_id is not None else ""}{" AND " if card_id is not None and card_name is not None else ""}{"card_name LIKE '%" + card_name + "%'" if card_name is not None else ""}{" AND " if (card_id is not None or card_name is not None) and desc is not None else ""}{"desc LIKE '%" + desc + "%'" if desc is not None else ""}{"AND " if (card_id is not None or card_name is not None or desc is not None) and pendulum_effect is not None else ""}{"pendulum_effect LIKE '%" + pendulum_effect + "%'" if pendulum_effect is not None else ""}{" AND " if (card_id is not None or card_name is not None or desc is not None or pendulum_effect is not None) and level_rank is not None else ""}{"level_rank = " + str(level_rank) if level_rank is not None else ""}{"AND " if (card_id is not None or card_name is not None or desc is not None or pendulum_effect is not None or level_rank is not None) and scale is not None else ""}{"scale = " + str(scale) if scale is not None else ""}{" AND " if (card_id is not None or card_name is not None or desc is not None or pendulum_effect is not None or level_rank is not None or scale is not None) and attack is not None else ""}{"attack = " + str(attack) if attack is not None else ""}{" AND " if (card_id is not None or card_name is not None or desc is not None or pendulum_effect is not None or level_rank is not None or scale is not None or attack is not None) and defense is not None else ""}{"defense = " + str(defense) if defense is not None else ""}{" AND " if (card_id is not None or card_name is not None or desc is not None or pendulum_effect is not None or level_rank is not None or scale is not None or attack is not None or defense is not None) and category_id is not None else ""}{"category_id = " + str(category_id) if category_id is not None else ""}{" AND " if (card_id is not None or card_name is not None or desc is not None or pendulum_effect is not None or level_rank is not None or scale is not None or attack is not None or defense is not None or category_id is not None) and card_type_id is not None else ""}{"card_type_id = " + str(card_type_id) if card_type_id is not None else ""}{" AND " if (card_type_id is not None or card_name is not None or desc is not None or pendulum_effect is not None or level_rank is not None or scale is not None or attack is not None or defense is not None or category_id is not None or card_type_id is not None) and attr_id is not None else ""}{"attr_id = " + str(attr_id) if attr_id is not None else ""}"""
        query_result = DB.execute_query(query, order=order, order_by=order_by, limit=limit)
        DB.disconnect()
        
        if query_result is None:
            return None
        
        if limit == 0 or limit > 1:
            result = []
            for i in query_result:
                result.append(Card(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], Card_Version.Card_Version().filter(card_id=i[0], empty='card'), Card_Link.Card_Link().filter(card_id=i[0], empty='card'), Card_SubCategory.Card_SubCategory().filter(card_id=i[0], empty='card'), Card_Deck.Card_Deck().filter(card_id=i[0], empty='card')))
            return result
        elif limit == 1:
            return Card(query_result[0], query_result[1], query_result[2], query_result[3], query_result[4], query_result[5], query_result[6],query_result[7], query_result[8], query_result[9], query_result[10], Card_Version.Card_Version().filter(card_id=query_result[0], empty='card'), Card_Link.Card_Link().filter(card_id=query_result[0], empty='card'), Card_SubCategory.Card_SubCategory().filter(card_id=query_result[0], empty='card'), Card_Deck.Card_Deck().filter(card_id=query_result[0], empty='card'))
        else:
            return None
        
    def change_into(self, card_id=None, empty=None):
        if card_id is None:
            self.card_id = None
            self.card_name = None
            self.desc = None
            self.pendulum_effect = None
            self.level_rank = None
            self.scale = None
            self.attack = None
            self.defense = None
            self.category = None
            self.type = None
            self.attr = None
            self.card_versions = []
            self.card_links = []
            self.card_subcategories = []
            self.card_decks = []
            return self
        
        DB.connect()
        query = f"SELECT * FROM `card` WHERE `card_id` = '{card_id}'"
        query_result = DB.execute_query(query, limit=1)
        DB.disconnect()
        
        if query_result is None:
            return None
        
        self.card_id = query_result[0]
        self.card_name = query_result[1]
        self.desc = query_result[2]
        self.pendulum_effect = query_result[3]
        self.level_rank = query_result[4]
        self.scale = query_result[5]
        self.attack = query_result[6]
        self.defense = query_result[7]
        self.category = Category().change_into(category_id=query_result[8])
        self.type = CardType().change_into(card_type_id=query_result[9])
        self.attr = Attribute().change_into(attr_id=query_result[10])
        if empty != 'version':
            self.card_versions = Card_Version.Card_Version().filter(card_id=query_result[0], empty='card')
        else:
            self.card_versions = []
        if empty != 'link':
            self.card_links = Card_Link.Card_Link().filter(card_id=query_result[0], empty='card')
        else:
            self.card_links = []
        if empty!= 'subcategory':
            self.card_subcategories = Card_SubCategory.Card_SubCategory().filter(card_id=query_result[0], empty='card')
        else:
            self.card_subcategories = []
        if empty!= 'deck' or empty!= 'deck_type':
            self.card_decks = Card_Deck.Card_Deck().filter(card_id=query_result[0], empty='card')
        else:
            self.card_decks = []
        
        return self
            
    def create(self, card_id, card_name, desc, category_id, card_type_id, pendulum_effect=None, level_rank=None, scale=None, attack=None, defense=None, attr_id=None):
        DB.connect()
        if card_name is not None:
            card_name = card_name.replace("'", "\\'")
        if desc is not None:
            desc = desc.replace("'", "\\'")
        if pendulum_effect is not None:
            pendulum_effect = pendulum_effect.replace("'", "\\'")
        query = f"""INSERT INTO `card`(`card_id`, `card_name`, `desc`, `category_id`, `card_type_id`{", `pendulum_effect`" if pendulum_effect is not None else ""}{", `level_rank`" if level_rank is not None else ""}{", `scale`" if scale is not None else ""}{", `attack`" if attack is not None else ""}{", `defense`" if defense is not None else ""}{", `attr_id`" if attr_id is not None else ""}) VALUES ('{card_id}', '{card_name}' , '{desc}', {str(category_id)}, {str(card_type_id)}{", '" + pendulum_effect + "'" if pendulum_effect is not None else ""}{", " + str(level_rank) if level_rank is not None else ""}{", " + str(scale) if scale is not None else ""}{", " + str(attack) if attack is not None else ""}{", " + str(defense) if defense is not None else ""}{", " + str(attr_id) if attr_id is not None else ""})"""
        query_result = DB.execute_query(query, limit=-1)
        DB.disconnect()
        
        if query_result is None:
            return None
        
        return self.change_into(query_result)
    
    def update(self, card_id=None, card_name=None, desc=None, pendulum_effect=None, level_rank=None, scale=None, attack=None, defense=None, category_id=None, card_type_id=None,attr_id=None):
        if (card_name is None and desc is None and pendulum_effect is None and level_rank is None and scale is None and attack is None and defense is None and category_id is None and card_type_id is None and attr_id is None) or (card_id is None and self.card_id is None):
            return self
        
        DB.connect()
        if card_name is not None:
            card_name = card_name.replace("'", "\\'")
        if desc is not None:
            desc = desc.replace("'", "\\'")
        if pendulum_effect is not None:
            pendulum_effect = pendulum_effect.replace("'", "\\'")
        query = f"""UPDATE `card` SET {"`card_name` = '" + card_name + "'" if card_name is not None else ""}{", " if card_name is not None and desc is not None else ""}{"`desc` = '" + desc + "'" if desc is not None else ""}{", " if (card_name is not None or desc is not None) and pendulum_effect is not None else ""}{"`pendulum_effect` = '" + pendulum_effect + "'" if pendulum_effect is not None else ""}{", " if (card_name is not None or desc is not None or pendulum_effect is not None) and level_rank is not None else ""}{"`level_rank` = " + str(level_rank) if level_rank is not None else ""}{", " if (card_name is not None or desc is not None or pendulum_effect is not None or level_rank is not None) and scale is not None else ""}{"`scale` = " + str(scale) if scale is not None else ""}{", " if (card_name is not None or desc is not None or pendulum_effect is not None or level_rank is not None or scale is not None) and attack is not None else ""}{"`attack` = " + str(attack) if attack is not None else ""}{", " if (card_name is not None or desc is not None or pendulum_effect is not None or level_rank is not None or scale is not None) and attack is not None else ""}{"`attack` = " + str(attack) if attack is not None else ""}{", " if (card_name is not None or desc is not None or pendulum_effect is not None or level_rank is not None or scale is not None or attack is not None) and defense is not None else ""}{"`defense` = " + str(defense) if defense is not None else ""}{", " if (card_name is not None or desc is not None or pendulum_effect is not None or level_rank is not None or scale is not None or attack is not None or defense is not None) and category_id is not None else ""}{"`category_id` = " + str(category_id) if category_id is not None else ""}{", " if (card_name is not None or desc is not None or pendulum_effect is not None or level_rank is not None or scale is not None or attack is not None or defense is not None or category_id is not None) and card_type_id is not None else ""}{"`card_type_id` = " + str(card_type_id) if card_type_id is not None else ""}{", " if (card_name is not None or desc is not None or pendulum_effect is not None or level_rank is not None or scale is not None or attack is not None or defense is not None or category_id is not None or card_type_id is not None) and attr_id is not None else ""}{"`attr_id` = " + str(attr_id) if attr_id is not None else ""} WHERE `card_id` = {str(card_id) if card_id is not None else str(self.card_id)}"""
        query_result = DB.execute_query(query)
        DB.disconnect()
        
        if query_result is None:
            return None
        
        return self.change_into(card_id =card_id if card_id is not None else self.card_id)
    
    def delete(self, card_id=None):
        if card_id is not None or self.card_id is not None: 
            Card_Version.Card_Version().delete(card_id=card_id if card_id is not None else self.card_id)
            Card_Link.Card_Link().delete(card_id=card_id if card_id is not None else self.card_id)
            Card_SubCategory.Card_SubCategory().delete(card_id=card_id if card_id is not None else self.card_id)
            Card_Deck.Card_Deck().delete(card_id=card_id if card_id is not None else self.card_id)
            DB.connect()
            query = f"DELETE FROM `card` WHERE `card_id` = {str(card_id) if card_id is not None else str(self.card_id)}"
            query_result = DB.execute_query(query)
            DB.disconnect()
            
            if query_result is None:
                return None
        
        return self.change_into()
    