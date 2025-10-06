from fastapi import FastAPI
from .routers import links
from .database import engine
from . import models
from fastapi.middleware.cors import CORSMiddleware

# Cria as tabelas no banco de dados (se não existirem)
# Em um projeto real, isso seria feito com uma ferramenta de migração como Alembic
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Link Aggregator API")

origins = [
    "http://localhost:5173",  # A URL do seu app React em desenvolvimento rodando localmente
    "https://link-aggregator-frontend.vercel.app", # Adicionaremos a URL de produção aqui depois
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"], # Permite todos os métodos (GET, POST, etc.)
    allow_headers=["*"], # Permite todos os cabeçalhos
)


# Inclui as rotas definidas no arquivo de routers
app.include_router(links.router)

@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Bem-vindo à API do Agregador de Links! Estou vivo."}