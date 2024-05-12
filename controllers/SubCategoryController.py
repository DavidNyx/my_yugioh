import sys
sys.path.append('./')
from models.SubCategory import SubCategory

class SubCategoryController(SubCategory):
    def __init__(self, subcategory_id: int = None, subcategory_name: str = None):
        super().__init__(subcategory_id, subcategory_name)
        
    def all(self):
        return super().all()
    
    def filter(self, subcategory_id=None, subcategory_name=None, first=False):
        return super().filter(subcategory_id, subcategory_name, first)
    
    def create(self, subcategory_name):
        return super().create(subcategory_name)
    
    def update(self, subcategory_name, subcategory_id=None):
        return super().update(subcategory_name, subcategory_id)
    
    def delete(self, subcategory_id=None):
        return super().delete(subcategory_id)

