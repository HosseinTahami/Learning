from fastapi import FastAPI, Path, Query, HTTPException, status
from pydantic import BaseModel, Field
from typing import Optional


app = FastAPI()


class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int
    published_date: str

    def __init__(self, id, title, author, description, rating, published_date):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date = published_date


class BookRequest(BaseModel):
    id: Optional[int] = Field(default=None, title="id is not needed !")
    title: str = Field(min_length=3)
    author: str = Field(min_length=5)
    description: str = Field(min_length=5, max_length=100)
    rating: int = Field(ge=0, le=5)
    published_date: int

    class Config:
        json_schema_extra = {
            "example": {
                "title": "A New Book",
                "author": "John Smith",
                "description": "A few words about the book!",
                "rating": 5,
                "published_date": 2021,
            }
        }


BOOKS = [
    Book(
        1,
        "Django for beginners",
        "Hossein",
        "Django book for beginners!",
        5,
        2021,
    ),
    Book(
        2,
        "Django for professionals",
        "Hossein",
        "Django book for professionals!",
        5,
        2018,
    ),
    Book(
        3,
        "Django for writing api",
        "Hossein",
        "Django book for writing API!",
        5,
        2014,
    ),
    Book(
        4,
        "FastAPI for Beginners",
        "Tahami",
        "FastAPI book for beginners!",
        4,
        2023,
    ),
    Book(
        5,
        "FastAPI for Professionals",
        "Tahami",
        "FastAPI book for professionals!",
        3,
        2020,
    ),
    Book(
        6,
        "Flask for Beginners",
        "Seyed Hossein",
        "Flask book for beginners!",
        2,
        2021,
    ),
    Book(
        7,
        "Flask for Professionals",
        "Seyed Hossein",
        "Flask book for professionals!",
        3,
        2021,
    ),
]


@app.get("/books", status_code=status.HTTP_200_OK)
async def read_all_books():
    return BOOKS


@app.get("/books/{book_id}", status_code=status.HTTP_200_OK)
async def read_book(book_id: int = Path(gt=0)):
    for book in BOOKS:
        if book.id == book_id:
            return book
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Item not found !"
    )


@app.get("/books/", status_code=status.HTTP_200_OK)
async def read_books_by_published_date(published_date: int = Query(ge=1999, le=2025)):
    books_to_return = []
    for book in BOOKS:
        if book.published_date == published_date:
            books_to_return.append(book)
    return books_to_return


@app.get("/books/published/", status_code=status.HTTP_200_OK)
async def read_book_by_rating(book_rating: int = Query(ge=0, le=5)):
    books_to_return = []
    for book in BOOKS:
        if book.rating == book_rating:
            books_to_return.append(book)
    return books_to_return



@app.post("/create_book", status_code=status.HTTP_201_CREATED)
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.model_dump())
    BOOKS.append(find_book_id(new_book))


def find_book_id(book: Book):
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    return book


@app.put("/books/update_book", status_code=status.HTTP_204_NO_CONTENT)
async def update_book(updated_book: BookRequest):
    book_updated = False
    for i, book in enumerate(BOOKS):
        if updated_book.id == book.id:
            BOOKS[i] = updated_book
            book_updated = True
    if not book_updated:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item not found!"
        )


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int = Path(gt=0)):
    book_deleted = False
    for i, book in enumerate(BOOKS):
        if book.id == book_id:
            BOOKS.pop(i)
            book_deleted = True
            break
    if not book_deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item not found!"
        )
