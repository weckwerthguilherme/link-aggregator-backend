from fastapi import FastAPI
from .routers import links
from .database import engine
from . import models

# Cria as tabelas no banco de dados (se não existirem)
# Em um projeto real, isso seria feito com uma ferramenta de migração como Alembic
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Link Aggregator API")

# Inclui as rotas definidas no arquivo de routers
app.include_router(links.router)

@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Bem-vindo à API do Agregador de Links! Estou vivo."}