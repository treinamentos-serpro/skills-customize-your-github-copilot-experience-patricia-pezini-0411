# 📘 Atividade: Testes Automatizados e Tratamento de Erros

## 🎯 Objetivo

Pratique testes automatizados com `unittest` para verificar funções de processamento de texto e endpoints de uma API FastAPI. Use casos válidos e inválidos para confirmar que erros são comunicados de forma previsível.

## 📝 Tarefas

### 🛠️ Escrever testes para funções de texto

#### Descrição
Complete os testes de `normalize_text()` e `count_words()` no arquivo inicial. Use entradas comuns e também texto vazio para conferir o comportamento esperado.

#### Requisitos
O programa concluído deve:

- Verificar que `normalize_text()` remove espaços nas bordas, ignora linhas vazias e converte o texto para minúsculas
- Verificar que `count_words()` conta palavras repetidas sem diferenciar maiúsculas de minúsculas
- Incluir pelo menos uma asserção para uma entrada vazia

### 🛠️ Testar respostas da API

#### Descrição
Use `TestClient` para testar os endpoints da coleção de livros sem iniciar um servidor. Instale as dependências com `python -m pip install fastapi httpx` e execute os testes com `python starter-code.py`.

#### Requisitos
O programa concluído deve:

- Verificar que `GET /books` retorna status `200` e os livros esperados
- Verificar que `GET /books/{book_id}` retorna o livro existente
- Verificar que uma busca por um livro inexistente retorna status `404`
- Verificar que `POST /books` cria um livro e retorna status `201`

### 🛠️ Verificar validação e isolamento dos testes

#### Descrição
Acrescente testes para entradas inválidas e confirme que cada teste começa com a coleção em seu estado inicial, sem depender da ordem de execução.

#### Requisitos
O programa concluído deve:

- Verificar que `POST /books` sem um campo obrigatório retorna status `422`
- Verificar a mensagem de erro ou os detalhes de validação retornados pela API
- Restaurar os dados de exemplo antes de cada teste da API
- Executar a suíte completa com `python starter-code.py` sem falhas
