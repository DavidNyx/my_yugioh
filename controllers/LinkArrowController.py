import sys
sys.path.append('./')
from models.LinkArrow import LinkArrow

class LinkArrowController(LinkArrow):
    def __init__(self, link_arrow_id: int = None, link_arrow_name: str = None):
        super().__init__(link_arrow_id, link_arrow_name)
        
    def all(self):
        return super().all()
    
    def filter(self, link_arrow_id=None, link_arrow_name=None, first=False):
        return super().filter(link_arrow_id, link_arrow_name, first)
    
    def create(self, link_arrow_name):
        return super().create(link_arrow_name)
    
    def update(self, link_arrow_name, link_arrow_id=None):
        return super().update(link_arrow_name, link_arrow_id)
    
    def delete(self, link_arrow_id=None):
        return super().delete(link_arrow_id)

