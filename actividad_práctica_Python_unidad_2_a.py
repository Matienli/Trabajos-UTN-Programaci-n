print("Ejercicio N°1")
edad = int(input("Ingrese su edad: "))

if edad == 18:
    print("Usted tiene 18 años")
else:
    print ("Usted no tiene 18 años")

print()
print ("Ejercicio N°2")
edad_1= int(input("Ingrese su edad, porfavor: "))
if edad_1 >= 18:
    print("MAYOR")
else: 
    print("MENOR")

print()
print ("Ejercicio N°3")
altura= float(input("Ingrese su altura en metros: "))
if altura >= 1.80:
    print ("Usted puede ser pivot")
else:
    print ("Usted no puede ser pivot")

print()
print ("Ejercicio N°4")
edad_2= int(input("Ingrese su edad: "))
if edad_2 >= 13 and edad_2 <= 17:
    print ("Usted es adolescente")
else: 
    print ("Usted no es adolescente")

print()
print ("Ejercicio N°5")
edad_3= int(input("Ingrese su edad: "))
if edad_3 <10:
    print("Eres un niño")
elif edad_3 >= 10 and edad_3 <13:
    print("Eres un pre-adolescente")
elif edad_3 >= 13 and edad_3 <=17:
    print ("Eres un adolescente")
elif edad_3 >= 18:
    print("Eres mayor de edad")


