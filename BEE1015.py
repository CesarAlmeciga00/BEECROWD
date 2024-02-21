from math import sqrt
x = input()
y = input()

listaX = x.split()
listaY = y.split()

x1 = float(listaX[0])
y1 = float(listaX[1])
x2 = float(listaY[0])
y2 = float(listaY[1])


resultado = sqrt((x2-x1)**2 + (y2-y1)**2)


print(f"{format(resultado,'.4f')}")