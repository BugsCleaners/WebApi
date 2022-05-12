from fastapi import FastAPI, HTTPException
from model import BookNoID
from model import Book

BOOKS = [
 Book(id=1, title="How to be a Monk", author="Scarlet Johnson"),
 Book(id=2, title="The Life of a Marmadillo", author="Thief Brat"),
 Book(id=3, title="Ethics Volume 1", author="Aristotle")
  ]

app = FastAPI()

@app.get("/")
async def get_all():
    return BOOKS

@app.post("/create")
async def create_book(book: Book, id: int):
    BOOKS.append(book)
    return book 


@app.put("/{book_id}")
async def update_book(book_id: int, book: BookNoID):
    counter = 0
    for x in BOOKS:
        counter += 1
        if x.id == book_id:
            BOOKS[counter - 1] = Book(id=book_id, title=book.title, author=book.author, description=book.description)

            return BOOKS[counter - 1]
    
    raise HTTPException(status_code=404,
                        detail="Book Not Found",
                        headers={"X-Header-Error": "Nothing to be seen at the ID"})    


@app.delete("/{book_id}")
async def delete_book(book_id: int):
    counter = 0
    for x in BOOKS:
        counter += 1
        if x.id == book_id:
            del BOOKS[counter - 1]
            return f'ID:{book_id} deleted.'
    
    raise HTTPException(status_code=404,
                        detail="Book Not Found",
                        headers={"X-Header-Error": "Nothing to be seen at the ID"})    