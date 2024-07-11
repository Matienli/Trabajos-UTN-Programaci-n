print("Ejercicio 1")
suma_pares= 0
for numero in range(1, 11):
    
    if numero % 2 == 0:
        
        suma_pares += numero

print("La suma de los números pares entre 1 y 10 es:", suma_pares)

print ()
print ("Ejercicio 2")
contraseña_correcta= "utn750"
contraseña = input ("Ingrese su contraseña: ")
while contraseña != contraseña_correcta:
    print ("Contraseña incorrecta")
    contraseña = input ("Ingrese nuevamente su contraseña: ")

print ("Contraseña correcta")

print ()
print ("Ejercicio 3")
numero_solicitado= int (input("Ingrese un numero: "))
while numero_solicitado < 0 or numero_solicitado > 9:
    print ("Numero incorrecto")
    numero_solicitado= int (input ("Vuelve a ingresar un numero: "))

print ("Numero correcto")

print ()
print ("Ejercicio 4")
letra_solicitada= input("Ingrese una letra en mayuscula: ")
while letra_solicitada != "U" and letra_solicitada != "T" and letra_solicitada != "N":
    print ("Letra incorrecta")
    letra_solicitada = input ("Ingrese nuevamente una letra en mayuscula: ")

print ("Letra correcta")

print ()
print ("Ejercicio 5")
numero_1= int(input("Ingrese el primer numero: "))
numero_2= int(input("Ingrese el segundo numero: "))
numero_3= int(input("Ingrese el tercero numero: "))
numero_4= int(input("Ingrese el cuarto numero: "))
numero_5= int(input("Ingrese el quinto numero: "))
suma_acumulada= numero_1 + numero_2 + numero_3 + numero_4 + numero_5
promedio= (suma_acumulada) / 5
print (suma_acumulada)
print ("El promedio de los numero ingresados es: ", promedio)
