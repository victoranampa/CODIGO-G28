while True:
  print("\nMINI CALCULADORA")
  print("="*28)
  primer_numero = int(input("Ingreso el primer número: "))
  segundo_numero = int(input("Ingreso el segundo número: "))
  operacion = input("Ingrese la operación: ")

  if operacion == "SUMA":
    resultado = primer_numero + segundo_numero
  elif operacion == "RESTA":
    resultado == primer_numero - segundo_numero  
  elif operacion == "MULTIPLICACION":
    resultado = primer_numero * segundo_numero
  elif operacion == "DIVISION":
    resultado = primer_numero / segundo_numero
  else:
    print("Operacion incorrecta")
    continue

  print (f"El resultado es {resultado}")
