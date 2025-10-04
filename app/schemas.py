from typing import Optional

from pydantic import BaseModel
from datetime import datetime

#Schema base com campos comuns
class LinkBase(BaseModel):
    title: str
    url: str
    display_order: int = 0

# Schema para a criação de um novo link (não precisa do id)
class LinkCreate(LinkBase):
    pass

# Schema para a leitura de um link (inclui campos do banco como id e created_at)
class Link(LinkBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True # Permite que o Pydantic leia o modelo SQLAlchemy

#Schema para a edição dos links
class LinkUpdate(BaseModel):
    title: Optional[str] = None
    url: Optional[str] = None
    display_order: Optional[int] = None
