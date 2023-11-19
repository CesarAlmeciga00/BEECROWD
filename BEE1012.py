lista_a = input()
elementos_a = lista_a.split()

print(f"TRIANGULO: {format((float(elementos_a[0]) * float(elementos_a[2])/2),'.3f')}")
print(f"CIRCULO: {format(3.14159*float(elementos_a[2])**2,'.3f')}")
print(f"TRAPEZIO: {format(((float(elementos_a[0])+float(elementos_a[1]))*float(elementos_a[2]))/2,'.3f')}")
print(f"QUADRADO: {format(float(elementos_a[1])**2,'.3f')}")
print(f"RETANGULO: {format((float(elementos_a[1])*float(elementos_a[0])),'.3f')}")
