lista_a = input()
elementos_a = lista_a.split()
lista_b = input()
elementos_b = lista_b.split()

resultado = (int((elementos_a[1]))*float(elementos_a[2]))+(int(elementos_b[1])*float(elementos_b[2]))
print(f"VALOR A PAGAR: R$ {format(resultado,'.2f')}")