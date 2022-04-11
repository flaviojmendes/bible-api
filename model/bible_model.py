
from ast import Str
from lib2to3.pytree import Base
from typing import List, Optional
from pydantic import BaseModel


class Chapter(BaseModel):
    verses: List[str] = []


class Book(BaseModel):
    name: str
    chapters: str
    abbrev: str


class Testament(BaseModel):
    name: str
    abbrev: str
    books: Optional[List[Book]] = []


class Verse(BaseModel):
    book: str
    chapter: int
    verse: int
    text: str
