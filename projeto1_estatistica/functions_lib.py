import pandas as pd
import matplotlib.pyplot as plt
from math import sqrt

def dado(lista, chave, index=162):
    return lista[chave][index:]

def boxplot (lista, title):
    listaTemp = []
    for i in lista:
        listaTemp.append(i)
    plt.boxplot(listaTemp)
    plt.title(title)
    
def histograma(lista, title):
    plt.hist(lista, bins='auto')
    plt.title(title)
    
def describe(lista, title):
    print(DMA(lista,title))
    print(CV(lista,title))    
    print (pd.DataFrame.describe(lista))
    
def DMA(listaDado, title):
    media = sum(listaDado) / len(listaDado)
    dma = 0
    for i in listaDado:
        modulodif = sqrt((i-media)**2)
        dma += (1/len(listaDado))* modulodif
    return "DMA is", dma 
    
def CV(listaDado, title):
    media = sum(listaDado) / len(listaDado)
    cv = 0
    for i in listaDado:
        cv = (1/len(listaDado))*(i-media)**2
    return "CV is", cv
    
def ifs (condicao, funcao, lista, listanomedado):
    print('De que grupo de dados deseja observar o ')
    var = input('Brazil\nCeará\nMinas Gerais\nParaná\nRio de Janeiro\n')
    var = var.upper()
    if var == "CEARA":
        funcao(dado(lista, "Ceará"), listanomedado[0])
    elif var == listanomedado[1].upper():
        funcao(dado(lista,"Minas Gerais"), listanomedado[1])
    elif var == listanomedado[2].upper():
        funcao(dado(lista,"Rio de Janeiro"), listanomedado[2])
    elif var == listanomedado[3].upper():
        funcao(dado(lista,"Paraná"), listanomedado[3])
    elif var == listanomedado[4].upper():
        funcao(dado(lista,"Brazil"), listanomedado[4])
    else:
        print("alternativa incorreta")
        