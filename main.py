import os
from fastapi import FastAPI
from model.book_model import BookModel, ChapterModel, ParagraphModel
from model.search_model import SearchModel
from service.bible_service import BibleService
from service.youtube_service import YoutubeService
import uvicorn

from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware

app = FastAPI()
origins = ["*"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.add_middleware(GZipMiddleware)


@app.post("/search")
async def search_video(searchModel: SearchModel):
    result = YoutubeService().search_video_by_text(searchModel.search_term).result()
    return result


@app.get("/bible")
async def get_bible():
    return await BibleService().get_bible()


@app.get("/bible/{book}/{chapter}")
async def get_chapter(book: str, chapter: int):
    return await BibleService().get_chapter(book, chapter)


@app.get("/bible/random-verse")
async def get_chapter():
    return await BibleService().get_random_verse()


@app.get("/book/{book_id}")
async def get_book(book_id: int):
    # MOCKED BOOK
    paragraph1 = ParagraphModel(text="Uma noite destas, vindo da cidade para o Engenho Novo, encontrei num trem da Central um rapaz aqui do bairro, que eu conheço de vista e de chapéu. Cumprimentou-me, sentou-se ao pé de mim, falou da lua e dos ministros, e acabou recitando-me versos. A viagem era curta, e os versos pode ser que não fossem inteiramente maus. Sucedeu, porém, que, como eu estava cansado, fechei os olhos três ou quatro vezes; tanto bastou para que ele interrompesse a leitura e metesse os versos no bolso.")
    paragraph2 = ParagraphModel(text="Vi-lhe fazer um gesto para tirá-los outra vez do bolso, mas não passou do gesto; estava amuado. No dia seguinte entrou a dizer de mim nomes feios, e acabou alcunhando-me Dom Casmurro. Os vizinhos, que não gostam dos meus hábitos reclusos e calados, deram curso à alcunha, que afinal pegou. Nem por isso me zanguei. Contei a anedota aos amigos da cidade, e eles, por graça, chamam-me assim, alguns em bilhetes: Dom Casmurro, domingo vou jantar com você. Vou para Petrópolis, Dom Casmurro; a casa é a mesma da Renania; vê se deixas essa caverna do Engenho Novo, e vai lá passar uns quinze dias comigo. - Meu caro Dom Casmurro, não cuide que o dispenso do teatro amanhã; venha e dormirá aqui na cidade; dou-lhe camarote, dou-lhe chá, dou-lhe cama; só não lhe dou moça.")
    paragraph3 = ParagraphModel(text="Não consultes dicionários. Casmurro não está aqui no sentido que eles lhe dão, mas no que lhe pôs o vulgo de homem calado e metido consigo. Dom veio por ironia, para atribuir-me fumos de fidalgo. Tudo por estar cochilando! Também não achei melhor título para a minha narração — se não tiver outro daqui até ao fim do livro, vai este mesmo. O meu poeta do trem ficará sabendo que não lhe guardo rancor. E com pequeno esforço, sendo o título seu, poderá cuidar que a obra é sua. Há livros que apenas terão isso dos seus autores; alguns nem tanto.")
    paragraph4 = ParagraphModel(
        text="Agora que expliquei o título, passo a escrever o livro. Antes disso, porém, digamos os motivos que me põem a pena na mão.")
    paragraph5 = ParagraphModel(text="Vivo só, com um criado. A casa em que moro é própria; fi-la construir de propósito, levado de um desejo tão particular que me vexa imprimi-lo, mas vá lá. Um dia. há bastantes anos, lembrou-me reproduzir no Engenho Novo a casa em que me criei na antiga Rua de Mata-cavalos, dando-lhe o mesmo aspecto e economia")

    chapter1 = ChapterModel(title="CAPÍTULO I", paragraphs=[
                            paragraph1, paragraph2, paragraph3])
    chapter2 = ChapterModel(title="CAPÍTULO II", paragraphs=[paragraph4])

    book = BookModel(id=1, title="Dom Casmurro", chapters=[chapter1, chapter2])

    return book

if __name__ == '__main__':
    if(os.environ["ENV"] == 'prod'):
        uvicorn.run("main:app",
                    host="0.0.0.0",
                    port=8000,
                    reload=True,
                    ssl_keyfile=os.environ["PRIVATE_KEY"],
                    ssl_certfile=os.environ["CERT"]
                    )
    else:
        uvicorn.run("main:app",
                    host="0.0.0.0",
                    port=8000,
                    reload=True
                    )