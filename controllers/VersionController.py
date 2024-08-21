import sys
sys.path.append('./')
from models.Version import Version

class VersionController(Version):
    def __init__(self, version_id: int = None, version_name: str = None, card_versions:list = []):
        super().__init__(version_id, version_name, card_versions)
        
    def all(self, order='version_name', order_by='ASC', limit=0):
        return super().all(order, order_by, limit)
    
    def filter(self, version_id=None, version_name=None, order='version_name', order_by='ASC', limit=0):
        return super().filter(version_id, version_name, order, order_by, limit)
    
    def change_into(self, version_id=None):
        return super().change_into(version_id)
    
    def create(self, version_name):
        return super().create(version_name)
    
    def update(self, version_name, version_id=None):
        return super().update(version_name, version_id)
    
    def delete(self, version_id=None):
        return super().delete(version_id)

