import math 
import pandas as pd
import numpy as np
import scipy.spatial as sp
import sklearn as sk
from sklearn.neighbors import NearestNeighbors
from scipy.spatial import distance
import matplotlib.pyplot as plt

piza = pd.read_csv('pizza.csv')

nati = piza.iloc[0]
isa = piza.iloc[1]
jose = piza.iloc[2]
alejo = piza.iloc[3]
camilo = piza.iloc[4]
nata = piza.iloc[5]
pau = piza.iloc[6]
lina = piza.iloc[7]
sanin = piza.iloc[8]
salo = piza.iloc[9]

ANATI=[]
AISA=[]
AJOSE=[]
AALEJO=[]
ACAMILO=[]
ANATA=[]
APAU=[]
ALINA=[]
ASANIN=[]
ASALO=[]

for i in nati:
    ANATI.append(i)
for i in isa:
    AISA.append(i)
for i in jose:
     AJOSE.append(i)
for i in alejo:
    AALEJO.append(i)
for i in camilo:
    ACAMILO.append(i)
for i in nata:
    ANATA.append(i)
for i in pau:
    APAU.append(i)
for i in lina:
    ALINA.append(i)
for i in sanin:
    ASANIN.append(i)
for i in salo:
     ASALO.append(i)

all = [ANATI,AISA,AJOSE,AALEJO,ACAMILO,ANATA,APAU,ALINA,ASANIN,ASALO]

for item in all:
    item.pop(0)

av = math.sqrt(len(ASALO)) 


def jum (a):
  
    som =""
    if a == 0:
        som="nati"
    if a == 1:
        som="isa"
    if a == 2:
        som="jose"
    if a == 3:
        som="alejo"
    if a == 4:
        som="camilo"
    if a == 5:
        som="nata"
    if a == 6:
        som="pau"
    if a == 7:
        som="lina"
    if a == 8:
        som="sanin"
    if a == 9:
        som="salo"
    return som

jam = NearestNeighbors(n_neighbors=10,algorithm='ball_tree').fit(all)
distance, can = jam.kneighbors(all)
i = 0
for item in distance:
    print("Distancias de los usuarios con respecto al usuario ", jum(i), "\n", item)
    i += 1

f = 0
for item in can:
    print("Índices de los usuarios con respecto al usuario ", jum(f), " (Ordenados del más cercano al más lejano)", "\n", item)
    f += 1
 
    
y = 0



print("El eje X representa los índices de los usuarios, el eje Y representa las distancias")

for item in can:
    plt.rcParams["figure.figsize"] = [7.50, 3.50]
    plt.rcParams["figure.autolayout"] = True

    print("Usuario", jum(y))
    plt.title("Distancias de los usuarios con respecto a este usuario")
    plt.scatter(can[y], distance[y], color="blue")
    plt.show()
    y+=1
    
