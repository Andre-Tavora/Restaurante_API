# 🍔 Restaurant API + Data & AI Ready

API RESTful para gerenciamento de produtos de restaurante, desenvolvida com **FastAPI**, **SQLAlchemy** e **SQLite**, preparada para evolução para **Data Analytics e Inteligência Artificial**.

---

## 🚀 Visão Geral

Este projeto demonstra a construção de uma API backend moderna, com foco em:

- CRUD completo de produtos
- Persistência em banco relacional
- Arquitetura modular
- Integração futura com pipelines de dados e IA
- Boas práticas de versionamento com Git

---

## 🧠 Arquitetura

Cliente (Swagger / Frontend)  
↓  
FastAPI  
↓  
SQLAlchemy (ORM)  
↓  
SQLite  
↓  
(Evolução → PostgreSQL / Data Pipeline / ML)

---

## 🛠 Tecnologias

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Uvicorn
- Docker
- Git / GitHub

Em evolução:

- PostgreSQL
- Docker Compose
- Machine Learning
- APIs de recomendação

---

## 📂 Estrutura do Projeto

app/
├── database/
│ └── connection.py
├── models/
│ └── products.py
├── routers/
│ └── product_router.py
├── schemas/
│ └── product_schema.py
└── main.py

---

## ⚙️ Funcionalidades

✔ Criar produto  
✔ Listar produtos  
✔ Atualizar produto  
✔ Deletar produto

---

## 🔗 Endpoints

### GET /produtos

Lista todos os produtos cadastrados.

Exemplo de resposta:

[
{
"id": 1,
"nome": "Burger XR",
"preco": 29.9
}
]

---

### POST /produtos

Cria um novo produto.

Body:

{
"nome": "Burger XR",
"preco": 29.9
}

Resposta:

{
"id": 1,
"nome": "Burger XR",
"preco": 29.9
}

---

### PUT /produtos/{id}

Atualiza um produto existente.

Body:

{
"nome": "Burger XR Duplo",
"preco": 34.9
}

---

### DELETE /produtos/{id}

Remove um produto.

Resposta:

{
"mensagem": "Produto removido com sucesso"
}

---

## ▶️ Como executar localmente

1. Clone o projeto

git clone git@github.com:andreorganizacional/restaurant-api.git  
cd restaurant-api

2. Ambiente virtual

python -m venv venv  
venv\Scripts\activate

3. Instalar dependências

pip install -r requirements.txt

4. Rodar API

uvicorn app.main:app --reload

5. Acessar Swagger

http://127.0.0.1:8000/docs

---

## 🐳 Docker

Build:

docker build -t restaurant-api .

Run:

docker run -d -p 8000:8000 --name restaurant-api-container restaurant-api

---

## ☁️ Deploy

https://SEU-LINK.onrender.com/docs

---

## 📸 Preview

![Swagger](docs/swagger.png)

---

## 🔄 Workflow Git

- main
- develop
- feature/database

---

## 🧪 Roadmap

- [ ] PostgreSQL
- [ ] Docker Compose
- [ ] Pipeline de dados
- [ ] Machine Learning
- [ ] API de recomendação

---

## 👤 Autor

Carlos André Távora Soares

---

## 💡 Sobre

Projeto voltado para:

- Backend Python
- Dados
- Inteligência Artificial

Foco em vagas **Júnior**
