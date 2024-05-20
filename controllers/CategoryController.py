import sys
sys.path.append('./')
from models.Category import Category

class CategoryController(Category):
    def __init__(self, category_id: int = None, category_name: str = None):
        super().__init__(category_id, category_name)
        
    def all(self, order='category_name', order_by='ASC', limit=0):
        return super().all(order, order_by, limit)
    
    def filter(self, category_id=None, category_name=None, order='category_name', order_by='ASC', limit=0):
        return super().filter(category_id, category_name, order, order_by, limit)
    
    def change_into(self, category_id=None):
        return super().change_into(category_id)
    
    def create(self, category_name):
        return super().create(category_name)
    
    def update(self, category_name, category_id=None):
        return super().update(category_name, category_id)
    
    def delete(self, category_id=None):
        return super().delete(category_id)

