from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from .. import services, schemas
from ..database import get_db

router = APIRouter(
    prefix="/links",
    tags=["links"] # Agrupa os endpoints na documentação
)

@router.post("/", response_model=schemas.Link, status_code=201)
def create_new_link(link: schemas.LinkCreate, db: Session = Depends(get_db)):
    return services.create_link(db=db, link=link)

@router.get("/", response_model=List[schemas.Link])
def read_all_links(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    links = services.get_links(db, skip=skip, limit=limit)
    return links

@router.put("/{link_id}", response_model=schemas.Link)
def update_existing_link(link_id: int, link: schemas.LinkUpdate, db: Session = Depends(get_db)):
    updated_link = services.update_link(db=db, link_id=link_id, link_update=link)
    if updated_link is None:
        raise HTTPException(status_code=404, detail="Link not found")
    return updated_link


@router.delete("/{link_id}", response_model=schemas.Link)
def delete_existing_link(link_id: int, db: Session = Depends(get_db)):
    deleted_link = services.delete_link(db=db, link_id=link_id)
    if deleted_link is None:
        raise HTTPException(status_code=404, detail="Link not found")
    return deleted_link