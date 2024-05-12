import sys
sys.path.append('./')
from models.Version import Version

class VersionController(Version):
    def __init__(self, version_id: int = None, version_name: str = None):
        super().__init__(version_id, version_name)
        
    def all(self):
        return super().all()
    
    def filter(self, version_id=None, version_name=None, first=False):
        return super().filter(version_id, version_name, first)
    
    def create(self, version_name):
        return super().create(version_name)
    
    def update(self, version_name, version_id=None):
        return super().update(version_name, version_id)
    
    def delete(self, version_id=None):
        return super().delete(version_id)

