import sys
sys.path.append('./')
from models.Category import Category

class CategoryController(Category):
    def __init__(self, category_id: int = None, category_name: str = None):
        super().__init__(category_id, category_name)
        
    def all(self):
        return super().all()
    
    def filter(self, category_id=None, category_name=None, first=False):
        return super().filter(category_id, category_name, first)
    
    def create(self, category_name):
        return super().create(category_name)
    
    def update(self, category_name, category_id=None):
        return super().update(category_name, category_id)
    
    def delete(self, category_id=None):
        return super().delete(category_id)

