print("Calculadora Python")
print("Ingrese los números que desea operar")
numero1=int(input("Número 1: "))
numero2=int(input("Número 2: "))
operacion=input("Escribe +, -, * o /")
resultado= None
if operacion == "+":
    resultado = numero1 + numero2
elif operacion == "-":
    resultado = numero1 - numero2
elif operacion == "*":
    resultado = numero1 * numero2
elif operacion == "/":
    resultado = numero1 / numero2
else:
    print("Operación no válida")
if resultado != None:
    print("Resultado :",resultado)