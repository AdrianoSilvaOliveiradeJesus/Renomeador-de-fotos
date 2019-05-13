import os 
from pathlib import Path

mypath = Path().absolute()

files_JPG = []

#Lista de códigos de referência dos óculos
lista_codigo_oculos = []

#quantidade de óculos para ser catálogada
quantidade_de_oculos = int(input("Quantidade de óculos para catalogar: "))

#Quantidade de óculos já catalogado
contador = 0

while contador < quantidade_de_oculos:
    #Código de referencia do óculos
    código_referência = str(input("Código de Referência: "))
    #Adicionando código a lista da códigos
    lista_codigo_oculos.append(código_referência.upper())
    contador += 1

os.chdir(mypath)

lista = sorted(os.listdir())

for file in lista:
    if ".JPG" in file:
        files_JPG.append(file)

#numero do item
item=1

#index do item
itemIndex = 0

for (index,file) in enumerate(files_JPG):
    src=file
    novoNome=str(index + 1)+" "+lista_codigo_oculos[itemIndex]+".JPG"
    itemIndex+=1
    item += 1
    os.rename(src,novoNome)
    print(src + "->" + novoNome)
    if(item > quantidade_de_oculos):
        itemIndex = 0
        item = 0

full_directory = str(mypath)

caminho_separado = full_directory.split("/")
pasta = caminho_separado[len(caminho_separado) - 1]
pai = d = Path().resolve().parent

os.chdir(pai)

nome_nova_pasta = ""
lista_de_nomes = sorted(set(lista_codigo_oculos))
for NS in lista_de_nomes:
        if(nome_nova_pasta == ""):
                nome_nova_pasta = nome_nova_pasta + NS
        else:
                nome_nova_pasta = nome_nova_pasta + "," + NS

lista_de_pastas = os.listdir(pai)
for folder in lista_de_pastas:
       if folder == pasta:
               os.rename(folder,nome_nova_pasta)




#links de apoio 
#https://www.mkyong.com/python/python-how-to-list-all-files-in-a-directory/
#https://stackoverflow.com/questions/2491222/how-to-rename-a-file-using-python