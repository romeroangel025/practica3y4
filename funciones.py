import datetime

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

def sonIguales():
 num1= int(input("ingrese un numero: "))
 num2= int(input("ingrese un numero: "))
 num3= int(input("ingrese un numero: "))
 if (num1+num2 == num3 or num1+num3==num2 or num3+num1==num2):
   print("son iguales")
 else:
  print("son distintos")  
  
def diferenciaHoraria():
 hora = int(input("Ingrese la hora: "))
 minuto = int(input("Ingrese el minuto: "))
 segundo = int(input("Ingrese el segundo: "))

 hora_actual = datetime.datetime.now().time()
 diferencia = datetime.datetime.combine(datetime.date.today(), hora_actual) - datetime.datetime.combine(datetime.date.today(), datetime.time(hora, minuto, segundo))

 print("La diferencia entre el horario ingresado y la hora actual es:", diferencia)  

def entradas():
 entrada= int(input("Ingrese los tres digitos de su entrada: "))
 if entrada == 0:
   print("Por favor, diríjase a la administración para obtener una nueva entrada.")
 elif(entrada%2==0): 
  print("sala 1")
 else:
  print("sala 3")
  
 def buzones():
   
   while  > 0:
    expediente = int(input("Ingrese un numero positivo (0 para terminar): "))  
  