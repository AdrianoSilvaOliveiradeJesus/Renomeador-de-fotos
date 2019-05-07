import os,glob
from pathlib import Path

mypath = Path().absolute()

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

#numero do item
item=1

#index do item
itemIndex = 0

for (index,file) in enumerate(glob.glob('.JPG')):
    src=file
    novoNome=str(index + 1)+" "+lista_codigo_oculos[itemIndex]+".jpg"
    itemIndex+=1
    item += 1
    os.rename(src,novoNome)
    if(item > quantidade_de_oculos):
        itemIndex = 0
        item = 0
        





#links de apoio 
#https://www.mkyong.com/python/python-how-to-list-all-files-in-a-directory/
#https://stackoverflow.com/questions/2491222/how-to-rename-a-file-using-python