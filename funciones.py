
def reverso():

 string = input("Por favor, ingrese su palabra: ")

 string_revertido = string[::-1]

 if (string_revertido == string):
  return print(string, "\n Bingo!")
 else:
    return print(string_revertido)


def tabla_9():
  for numero in range(1, 11):
      print(".- ""9 *", numero, "=", numero*9, "\n")


def es_palindromo():
    numero_str = input("ingrese su numero:")
    # print(type(numero_str))
    longitud = len(numero_str)

    for i in range(longitud // 2):
      if numero_str[i] != numero_str[longitud - i - 1]:
       return print("no es un palindromo")

    return print("es un palindromo")


def mediaPositivos():
 suma = 0
 contador = 0 
 numero = int(input("Introduzca un número positivo (0 para terminar): "))
 while numero > 0:
 
  suma += numero
  contador += 1
  numero = int(input("Ingrese un numero positivo (0 para terminar): "))

 if contador == 0:
    print("Error no se puede calcular la media de 0 numeros ")
 else:
    media = int(suma / contador)
    print("La media de los números ingresados es:", media)
    
def sumaPares():
  suma=0
  for i in range(2,100,2):
      suma=i+suma
  print("La suma es:",suma)
sumaPares()