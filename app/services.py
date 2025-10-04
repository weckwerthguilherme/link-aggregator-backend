from sqlalchemy.orm import Session
from . import models, schemas

def create_link(db: Session, link: schemas.LinkCreate) -> models.Link:
    # Cria uma nova instância do modelo sqlalchemy
    db_link = models.Link(
        title=link.title,
        url=link.url,
        display_order=link.display_order
    )
    db.add(db_link)  # Adiciona à sessão
    db.commit()  # Comita a transação para o banco
    db.refresh(db_link)  # Atualiza o objeto db_link com os dados do banco (como o id)
    return db_link

def get_links(db: Session, skip: int = 0, limit: int = 100) -> list[models.Link]:
    return db.query(models.Link).order_by(models.Link.display_order).offset(skip).limit(limit).all()


def update_link(db: Session, link_id: int, link_update: schemas.LinkUpdate) -> models.Link | None:
    # 1. Busca o link existente no banco de dados
    db_link = db.query(models.Link).filter(models.Link.id == link_id).first()

    if db_link:
        # 2. Converte o schema Pydantic para um dicionário
        update_data = link_update.model_dump(exclude_unset=True)

        # 3. Itera sobre os dados enviados e atualiza o objeto do banco
        for key, value in update_data.items():
            setattr(db_link, key, value)

        db.commit()
        db.refresh(db_link)

    return db_link


def delete_link(db: Session, link_id: int) -> models.Link | None:
    # 1. Busca o link existente no banco de dados
    db_link = db.query(models.Link).filter(models.Link.id == link_id).first()

    if db_link:
        # 2. Deleta o objeto da sessão e comita
        db.delete(db_link)
        db.commit()

    return db_link

#Tudo pronto