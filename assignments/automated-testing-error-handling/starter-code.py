import re
import unittest
from collections import Counter

from fastapi import FastAPI, HTTPException, status
from fastapi.testclient import TestClient
from pydantic import BaseModel


def normalize_text(text: str) -> str:
    lines = (line.strip().lower() for line in text.splitlines())
    return "\n".join(line for line in lines if line)


def count_words(text: str) -> Counter[str]:
    return Counter(re.findall(r"\b[\w']+\b", text.lower()))


class Book(BaseModel):
    id: int
    title: str
    author: str


class BookCreate(BaseModel):
    title: str
    author: str


INITIAL_BOOKS = [
    Book(id=1, title="The Hobbit", author="J. R. R. Tolkien"),
    Book(id=2, title="Frankenstein", author="Mary Shelley"),
]
books = INITIAL_BOOKS.copy()
app = FastAPI(title="Books API")


@app.get("/books", response_model=list[Book])
def list_books() -> list[Book]:
    return books


@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int) -> Book:
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")


@app.post("/books", response_model=Book, status_code=status.HTTP_201_CREATED)
def create_book(book_data: BookCreate) -> Book:
    next_id = max((book.id for book in books), default=0) + 1
    book = Book(id=next_id, **book_data.model_dump())
    books.append(book)
    return book


client = TestClient(app)


class TextProcessingTests(unittest.TestCase):
    def test_normalize_text(self) -> None:
        self.fail("TODO: teste espaços extras, linhas vazias e letras maiúsculas")

    def test_count_words(self) -> None:
        self.fail("TODO: teste contagem sem diferenciar maiúsculas e entrada vazia")


class BooksApiTests(unittest.TestCase):
    def setUp(self) -> None:
        books.clear()
        books.extend(INITIAL_BOOKS)

    def test_list_books(self) -> None:
        self.fail("TODO: verifique o status e os livros retornados por GET /books")

    def test_get_existing_book(self) -> None:
        self.fail("TODO: verifique GET /books/1")

    def test_get_missing_book_returns_404(self) -> None:
        self.fail("TODO: verifique o status e o detalhe de um livro inexistente")

    def test_create_book(self) -> None:
        self.fail("TODO: verifique POST /books, o status 201 e o livro criado")

    def test_invalid_book_returns_422(self) -> None:
        self.fail("TODO: envie um livro sem autor e verifique a resposta 422")


if __name__ == "__main__":
    unittest.main(verbosity=2)
