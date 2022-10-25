
from pytube import YouTube

link = input('Qual video esta procurando?')
path = input("qual o caminho?")

yt = YouTube(link)

ress = {
    "Titulo": yt.title,
    "views": yt.views,
    "videos": yt.streams.filter(file_extension='mp4')
}
print(ress)
print("Selecione  a melhor qualidade.....")
YouD = yt.streams.get_by_itag(input("Qual id?")).download(path),
print("Baixando com sucesso!")
