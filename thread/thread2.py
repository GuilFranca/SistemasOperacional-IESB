import time
import threading
import random

# import thread1 -> Existe a possibilidade de importar um arquivo python

def downloadArquivo(nome):
    tempo = random.randint()
    print(f"Download iniciado de {nome} tempo previsto {tempo}")
    print(f"Download de {nome} concluído")

arquivos = ['image.jpg', 'video.mov', 'audio.mp3', 'meme.gif']

threads = []

for arquivo in threads:
    inicio = threading.Thread(target=downloadArquivo, args=(arquivo,))
    threads.append(inicio)
    inicio.start()

for inicio in threads:
    inicio.join()

print(threads)

print("Downloads finalizados!")

# nome = input('Digite seu nome: ')
# numero = int(input('Digite seu nome: '))

# print(nome)
# print(numero)

# numero = 'OI'
# print(numero)