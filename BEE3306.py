from math import gcd
from functools import reduce
import re
x = input()
listaX = x.split()
x1 = int(listaX[0])
x2 = int(listaX[1])

vector = input()
vector = vector.strip()
vector = vector.split()


for i in range(x2):
    try:
        query = input()
        queryList = query.split()
        if int(queryList[0]) == 1:
            lista = []
            for j in range(int(queryList[1])-1, int(queryList[2])):
                lista.append(j)
            for j in range(len(lista)):
                vector[int(lista[j])]= int(vector[int(lista[j])]) + int(queryList[3])
        elif int(queryList[0]) == 2:
            lista = []
            vectorF = []
            for j in range(int(queryList[1])-1, int(queryList[2])):
                lista.append(j)
            for j in range(len(lista)):
                vectorF.append(int(vector[int(lista[j])]))
            mcd = reduce(gcd,vectorF)
            print(mcd)
        else:
            print (f"{i+1}")
    except:
        print (f"{i+1}")

