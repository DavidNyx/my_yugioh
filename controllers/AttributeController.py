import sys
sys.path.append('./')
from models.Attribute import Attribute

class AttributeController(Attribute):
    def __init__(self, attr_id: int = None, attr_name: str = None):
        super().__init__(attr_id, attr_name)
        
    def all(self, order='attr_name', order_by='ASC', limit=0):
        return super().all(order, order_by, limit)
    
    def filter(self, attr_id=None, attr_name=None, order='attr_name', order_by='ASC', limit=0):
        return super().filter(attr_id, attr_name, order, order_by, limit)
    
    def change_into(self, attr_id=None):
        return super().change_into(attr_id)
    
    def create(self, attr_name):
        return super().create(attr_name)
    
    def update(self, attr_name, attr_id=None):
        return super().update(attr_name, attr_id)
    
    def delete(self, attr_id=None):
        return super().delete(attr_id)

