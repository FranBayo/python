#ejercicio1: si es mayor de edad = true
#   edad = int(input("Introduce una edad: "))
#se puede escribir 'EsMayorEdad = edad >= 18'
#   print("es mayor de edad?")
#   EsMayorEdad = (edad >= 18)
#   print(EsMayorEdad)
#   print(type(EsMayorEdad))
#   if EsMayorEdad: #también funciona poner la función directamente
#si no se tabula no ve lo que hay en el if
#       print ("Es mayor de edad")
#   else: #else siempre debajo de if, si no no funciona
#       print("Es menor de edad")
#   print("seimprime")
#ejercicio2: si es fin de semana = true
#   dia = input("Introduce un dia: ")
#   print("es fin de semana?")
#   print(dia == "Sabado" or dia == "Domingo")
#ejercicio3: si es un número positivo = true
#   mas = int(input("Introduce un numero: "))
#   print("es positivo?")
#   EsPositivo = (mas > 0)
#   if EsPositivo:
#       print("Es positivo")
#   elif mas < 0: #else if no funciona, tiene que ser elif
#       print("No es positivo")
#   else:
#       print("es cero")
#ejercicio4: si es vocal = true
#   letra = input("Introduce una letra: ")
#   print("es una vocal?")
#   print(letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U")
#ejercicio5: Nota aprobada = true (examen de 0 a 10)
nota = int(input("Introduce una nota: "))
print("está aprobada?")
if nota < 0 or nota > 10:
    print("No es una nota válida")
elif nota < 5:
    print("Estás suspenso")
elif nota < 7:
    print("Estás aprobado")
elif nota < 9:
    print("Has sacado buena nota")
elif nota == 9:
    print("Has sacado muy buena nota")
elif nota == 10:
    print("Has sacado sobresaliente")
