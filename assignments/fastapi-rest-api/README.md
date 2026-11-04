# 📘 Tarefa: Criando uma API REST com FastAPI

## 🎯 Objetivo

Construa uma API REST para gerenciar uma coleção de livros usando Python e FastAPI. Você praticará rotas HTTP, validação de dados e respostas apropriadas para recursos existentes ou não encontrados.

## 📝 Tarefas

### 🛠️ Consultar livros

#### Descrição
Implemente endpoints para listar todos os livros e consultar um livro pelo seu `id`.

#### Requisitos
O programa concluído deve:

- Retornar a coleção de livros em `GET /books`
- Retornar um livro em `GET /books/{book_id}`
- Responder com status HTTP 404 quando o livro solicitado não existir

### 🛠️ Adicionar livros

#### Descrição
Permita que clientes adicionem livros à coleção enviando dados em uma requisição HTTP.

#### Requisitos
O programa concluído deve:

- Criar um livro em `POST /books` usando o modelo `BookCreate`
- Validar os dados recebidos com Pydantic
- Retornar o livro criado com status HTTP 201 e um `id` único

### 🛠️ Atualizar e remover livros

#### Descrição
Complete as operações da API permitindo substituir ou remover um livro existente.

#### Requisitos
O programa concluído deve:

- Substituir os dados de um livro em `PUT /books/{book_id}`
- Remover um livro em `DELETE /books/{book_id}`
- Responder com status HTTP 404 ao tentar atualizar ou remover um livro inexistente

## ▶️ Como executar

Instale as dependências com `python -m pip install fastapi uvicorn` e inicie a API com `uvicorn starter-code:app --reload`. Acesse `/docs` no navegador para explorar e testar os endpoints interativamente.
