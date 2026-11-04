# 📘 Tarefa: Python Text Processing

## 🎯 Objetivo

Crie um programa Python que leia um arquivo de texto, normalize seu conteúdo e gere um resumo com estatísticas e palavras mais frequentes. A atividade pratica strings, manipulação de arquivos e transformação de texto.

## 📝 Tarefas

### 🛠️ Limpar e normalizar texto

#### Descrição
Implemente uma função que receba um texto e normalize espaços em branco e letras maiúsculas/minúsculas.

#### Requisitos
O programa concluído deve:

- Remover espaços extras no início e no fim das linhas
- Converter o texto para letras minúsculas
- Ignorar linhas vazias no resultado

### 🛠️ Ler um arquivo e analisar palavras

#### Descrição
Leia o arquivo `sample.txt` em UTF-8, normalize seu conteúdo e conte quantas vezes cada palavra aparece.

#### Requisitos
O programa concluído deve:

- Abrir o arquivo usando `pathlib.Path` e codificação UTF-8
- Contar palavras sem diferenciar letras maiúsculas e minúsculas
- Exibir o total de palavras e as cinco palavras mais frequentes

### 🛠️ Gerar um relatório de texto

#### Descrição
Salve os resultados da análise em um arquivo `report.txt` legível, com uma palavra por linha na lista de frequências.

#### Requisitos
O programa concluído deve:

- Salvar o relatório em UTF-8
- Incluir o total de palavras e as palavras mais frequentes com suas contagens
- Manter intacto o arquivo original `sample.txt`

## ▶️ Como executar

Coloque `starter-code.py` e `sample.txt` na mesma pasta e execute `python starter-code.py`. O programa deverá criar `report.txt` nessa pasta.
