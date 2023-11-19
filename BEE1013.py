maxNum = input()
lista = maxNum.split()
for a in range(len(lista)):
    lista[a] = int(lista[a])

mayor = max(lista)

print(f"{mayor} eh o maior")
