from pydantic import BaseModel
from typing import Optional

# -------- Genre Schemas --------

class GenreBase(BaseModel):
    name: str

class GenreCreate(GenreBase):
    pass

class GenreUpdate(GenreBase):
    pass

class Genre(GenreBase):
    id: int

    class Config:
        orm_mode = True

# -------- Author Schemas --------

class AuthorBase(BaseModel):
    full_name: str

class AuthorCreate(AuthorBase):
    pass

class AuthorUpdate(AuthorBase):
    pass

class Author(AuthorBase):
    id: int

    class Config:
        orm_mode = True

# -------- Book Schemas --------

class BookBase(BaseModel):
    title: str
    description: Optional[str] = None
    genre_id: int
    author_id: int

class BookCreate(BookBase):
    pass

class BookUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    genre_id: Optional[int] = None
    author_id: Optional[int] = None

class Book(BookBase):
    id: int
    genre: Genre
    author: Author

    class Config:
        orm_mode = True
