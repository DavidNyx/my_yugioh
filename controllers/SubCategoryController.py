import sys
sys.path.append('./')
from models.SubCategory import SubCategory

class SubCategoryController(SubCategory):
    def __init__(self, subcategory_id: int = None, subcategory_name: str = None, card_subcategories: list = []):
        super().__init__(subcategory_id, subcategory_name, card_subcategories)
        
    def all(self, order='subcategory_name', order_by='ASC', limit=0):
        return super().all(order, order_by, limit)
    
    def filter(self, subcategory_id=None, subcategory_name=None, order='subcategory_name', order_by='ASC', limit=0):
        return super().filter(subcategory_id, subcategory_name, order, order_by, limit)
    
    def change_into(self, subcategory_id=None):
        return super().change_into(subcategory_id)
    
    def create(self, subcategory_name):
        return super().create(subcategory_name)
    
    def update(self, subcategory_name, subcategory_id=None):
        return super().update(subcategory_name, subcategory_id)
    
    def delete(self, subcategory_id=None):
        return super().delete(subcategory_id)

