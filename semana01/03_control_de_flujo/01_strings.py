#String
texto = "Python es un lenguaje muy potente"

#Recorrer un string
for caracter in texto:
  print (caracter)

#Concatenar strings
texto_concatenado = texto + "y facil de aprender"
print (texto_concatenado)

#formatear Strings
nombre = "Pepito"
edad = 20
saludo = "Hola {}, tu edad es {} años".format(nombre, edad)
print(saludo)
segundo_saludo = f"hola {nombre}, tu edad es {edad} años"
print(segundo_saludo)
tercer_saludo = "Hola %s, tu edad es %d años" % (nombre, edad)
print(tercer_saludo)

#Metodos de strings

#.upper()
print("upper()", texto.upper())

print("lower()", texto.lower())

print("capitalize()", texto. capitalize())

print("count()", texto.count("Python"))

print("replace()", texto.replace("Python", "Rust"))

print("split()", texto.split(""))

# print()