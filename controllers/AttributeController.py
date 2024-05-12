import sys
sys.path.append('./')
from models.Attribute import Attribute

class AttributeController(Attribute):
    def __init__(self, attr_id: int = None, attr_name: str = None):
        super().__init__(attr_id, attr_name)
        
    def all(self):
        return super().all()
    
    def filter(self, attr_id=None, attr_name=None, first=False):
        return super().filter(attr_id, attr_name, first)
    
    def create(self, attr_name):
        return super().create(attr_name)
    
    def update(self, attr_name, attr_id=None):
        return super().update(attr_name, attr_id)
    
    def delete(self, attr_id=None):
        return super().delete(attr_id)

