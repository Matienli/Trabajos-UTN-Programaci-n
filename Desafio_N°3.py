numero = int(input("Ingrese un número: "))
print ("Número inicial: ", numero)
while True:
    numero += 1
    print (numero)
    if numero >=20:
        break
    #Lo hice hasta 20 para que no genere numeros infinitos
