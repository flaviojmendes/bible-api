from pydantic import BaseModel
from typing import List

class ParagraphModel(BaseModel):
    text: str

class ChapterModel(BaseModel):
    title: str
    paragraphs: List[ParagraphModel]

class BookModel(BaseModel):
    id: int
    title: str
    chapters: List[ChapterModel]

