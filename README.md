# 🍽️ Restaurante API

API de restaurante desenvolvida com **FastAPI + MongoDB**, com arquitetura organizada para cadastro e listagem de produtos.

Projeto focado em **Backend Python**, **APIs REST** e **integração com banco NoSQL**, ideal para portfólio de vaga **Desenvolvedor Python Júnior**.

---

# 🚀 Tecnologias

- Python
- FastAPI
- MongoDB
- PyMongo
- Uvicorn
- Pydantic
- Docker (opcional)

---

# 📁 Estrutura do Projeto

```
app/
├── database/
│   └── connection.py
├── models/
│   └── product_model.py
├── routers/
│   └── product_router.py
├── schemas/
│   └── product_schema.py
└── main.py
```

Arquitetura baseada em:

- Router layer
- Schema validation
- Model layer
- Database connection
- Clean architecture

---

# ⚙️ Instalação

Clone o projeto

```
git clone https://github.com/seu-repo/restaurante-api.git
cd RestauranteApi
```

Criar ambiente virtual

Windows

```
python -m venv venv
venv\Scripts\activate
```

Instalar dependências

```
pip install fastapi uvicorn pymongo python-dotenv
```

---

# 🗄️ Rodar MongoDB

Usando Docker:

```
docker run -d -p 27017:27017 --name mongodb mongo
```

Ou MongoDB local:

```
mongodb://localhost:27017
```

---

# ▶️ Executar API

```
uvicorn app.main:app --reload
```

---

# 📌 Acessar API

Swagger UI:

```
http://127.0.0.1:8000/docs
```

ReDoc:

```
http://127.0.0.1:8000/redoc
```

---

# 📦 Endpoints

## Criar produto

POST /products/

Body:

```
{
  "name": "Pizza Calabresa",
  "price": 39.9,
  "description": "Pizza grande"
}
```

---

## Listar produtos

GET /products/

Resposta:

```
[
  {
    "id": "6615f0b8a8c123456789abcd",
    "name": "Pizza Calabresa",
    "price": 39.9,
    "description": "Pizza grande"
  }
]
```

---

# 🧠 Conceitos aplicados

- FastAPI REST API
- MongoDB integration
- CRUD backend
- Router architecture
- Pydantic validation
- Clean code
- Backend structure profissional
- API documentation automática
- NoSQL database

---

# 🎯 Objetivo do Projeto

Projeto criado para portfólio de:

- Desenvolvedor Python Júnior
- Backend Developer
- AI / Data Backend
- FastAPI Developer
- MongoDB API Developer

---

# 👨‍💻 Autor

Carlos André Tavora Soares

Backend Developer | Python | FastAPI | AI | Computer Vision | MongoDB
