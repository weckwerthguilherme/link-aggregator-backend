# Link Aggregator - Backend

Este é o serviço de backend para a aplicação Link Aggregator, um projeto de agregador de links no estilo "Linktree", construído durante um fim de semana.

A API é responsável por gerenciar os links através de operações CRUD (Criar, Ler, Atualizar, Deletar) e persistir os dados em um banco de dados PostgreSQL.

## Tecnologias Utilizadas

* **Python 3.12+**
* **FastAPI:** Para a construção da API REST.
* **SQLAlchemy:** Como ORM para interação com o banco de dados.
* **PostgreSQL:** Banco de dados relacional. (Integrado no Render)
* **Pydantic:** Para validação de dados.
* **Gunicorn & Uvicorn:** Para servir a aplicação em produção.
* **Render:** Plataforma de nuvem para o deploy.

## Como Executar Localmente

1.  Crie e ative um ambiente virtual.
2.  Instale as dependências: `pip install -r requirements.txt`
3.  Crie um arquivo `.env` na raiz e adicione sua `DATABASE_URL`.
4.  Execute o servidor de desenvolvimento: `uvicorn app.main:app --reload`
