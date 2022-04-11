from typing import Dict, List
import requests

from model.bible_model import Book, Chapter, Testament, Verse
from dotenv import dotenv_values

class BibleService():
    
    def get_token(self):
        config = dotenv_values(".env") 
        return config['TOKEN']

    async def get_chapter(self, book_name: str, chapter_number: int) -> List[Chapter]:
        url = f'https://www.abibliadigital.com.br/api/verses/nvi/{book_name}/{chapter_number}'
        response = requests.get(url, headers={
                                'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6Ik1vbiBBcHIgMTEgMjAyMiAwOTo1NjowMiBHTVQrMDAwMC5mbGF2aW9qbWVuZGVzQGdtYWlsLmNvbSIsImlhdCI6MTY0OTY3MDk2Mn0.AVgPcTMfIrFduhHt5v0ytVmGbHJGENtnK1RIujM4bBE'})
        data = response.json()
        chapter_model = Chapter()
        for chapter in data['verses']:
            chapter_model.verses.append(chapter['text'])
        return chapter_model

    async def get_bible(self) -> Dict[str, Testament]:
        r = requests.get(url='https://www.abibliadigital.com.br/api/books', headers={
                         'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6Ik1vbiBBcHIgMTEgMjAyMiAwOTo1NjowMiBHTVQrMDAwMC5mbGF2aW9qbWVuZGVzQGdtYWlsLmNvbSIsImlhdCI6MTY0OTY3MDk2Mn0.AVgPcTMfIrFduhHt5v0ytVmGbHJGENtnK1RIujM4bBE'})
        data = r.json()
        books = {'vt': Testament(abbrev="vt", name="Velho Testamento"), 'nt': Testament(
            abbrev="vt", name="Novo Testamento")}

        for book in data:
            book_model = Book(
                name=book['name'], abbrev=book['abbrev']['pt'], chapters=book['chapters'])
            if book['testament'] == 'VT':
                books['vt'].books.append(book_model)
            else:
                books['nt'].books.append(book_model)

        return books

    async def get_random_verse(self) -> Verse:
        r = requests.get(url='https://www.abibliadigital.com.br/api/verses/nvi/random', headers={
                         'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6Ik1vbiBBcHIgMTEgMjAyMiAwOTo1NjowMiBHTVQrMDAwMC5mbGF2aW9qbWVuZGVzQGdtYWlsLmNvbSIsImlhdCI6MTY0OTY3MDk2Mn0.AVgPcTMfIrFduhHt5v0ytVmGbHJGENtnK1RIujM4bBE'})
        data = r.json()
        verse_model = Verse(book=data['book']['name'], chapter=data['chapter'], verse=data['number'], text=data['text'])
        return verse_model