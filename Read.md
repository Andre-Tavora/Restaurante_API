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

```
Cliente (Swagger / Frontend)
        ↓
     FastAPI
        ↓
   SQLAlchemy (ORM)
        ↓
     SQLite
        ↓
 (Evolução → PostgreSQL / Data Pipeline / ML)
```

---

## 🛠 Tecnologias

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Uvicorn
- Git / GitHub

🔜 Em evolução:

- PostgreSQL
- Docker
- Machine Learning
- APIs de recomendação

---

## 📂 Estrutura do Projeto

```
app/
├── database/
│   └── connection.py
├── models/
│   └── products.py
├── routers/
│   └── product_router.py
├── schemas/
│   └── product_schema.py
└── main.py
```

---

## ⚙️ Funcionalidades

✔ Criar produto
✔ Listar produtos
✔ Atualizar produto
✔ Deletar produto

---

## 🔗 Endpoints

### GET `/produtos`

Lista todos os produtos.

---

### POST `/produtos`

```json
{
  "nome": "Burger XR",
  "preco": 29.9
}
```

---

### PUT `/produtos/{id}`

```json
{
  "nome": "Burger XR Duplo",
  "preco": 34.9
}
```

---

### DELETE `/produtos/{id}`

Remove um produto pelo ID.

---

## ▶️ Como executar

### 1. Clone o projeto

```bash
git clone git@github.com:andreorganizacionalUSUARIO/restaurant-api.git
cd restaurant-api
```

---

### 2. Ambiente virtual

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

---

### 4. Rodar API

```bash
uvicorn app.main:app --reload
```

---

### 5. Acessar Swagger

```
http://127.0.0.1:8000/docs
```

---

## 📸 Preview

Adicione aqui um print do Swagger:

```
![Swagger](docs/swagger.png)
```

---

## 🔄 Workflow Git

Branches utilizadas:

- main
- develop
- feature/database

---

## 🧪 Roadmap (Evolução para Dados e IA)

Este projeto será expandido para incluir:

- [ ] Migração para PostgreSQL
- [ ] Containerização com Docker
- [ ] Pipeline de dados
- [ ] Análise de vendas
- [ ] Sistema de recomendação de produtos
- [ ] Machine Learning para previsão de demanda
- [ ] Integração com APIs de IA

---

## 📊 Visão futura (Data + IA)

O projeto evolui para um cenário completo de dados:

- tratamento de dados
- análise de vendas
- comportamento de clientes
- previsão de demanda
- recomendação de produtos

---

## 👤 Autor

Carlos André Távora Soares

---

## 💡 Sobre

Projeto desenvolvido como parte da construção de portfólio em:

- Backend Python
- Dados e Analytics
- Inteligência Artificial

Foco em oportunidades de **Desenvolvedor Júnior / IA / Dados**
