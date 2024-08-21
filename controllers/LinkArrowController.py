import sys
sys.path.append('./')
from models.LinkArrow import LinkArrow

class LinkArrowController(LinkArrow):
    def __init__(self, link_arrow_id: int = None, link_arrow_name: str = None, card_links: list = []):
        super().__init__(link_arrow_id, link_arrow_name, card_links)
        
    def all(self, order='link_arrow_name', order_by='ASC', limit=0):
        return super().all(order, order_by, limit)
    
    def filter(self, link_arrow_id=None, link_arrow_name=None, order='link_arrow_name', order_by='ASC', limit=0):
        return super().filter(link_arrow_id, link_arrow_name, order, order_by, limit)
    
    def change_into(self, link_arrow_id=None):
        return super().change_into(link_arrow_id)
    
    def create(self, link_arrow_name):
        return super().create(link_arrow_name)
    
    def update(self, link_arrow_name, link_arrow_id=None):
        return super().update(link_arrow_name, link_arrow_id)
    
    def delete(self, link_arrow_id=None):
        return super().delete(link_arrow_id)

