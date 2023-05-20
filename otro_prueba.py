'''un ejercicio de cuantos caracteres tiene una
cadena de texto contando los blancos

texto = input("Ingrese su texto: ")
cant = 0

for x in texto:
    cant = cant + 1
    
print (f"La cantidad de caracteres es: {cant}")
'''
'''#un ejercicio de cuanto palabras tiene una cadena de texto contando los blancos
t = input("Ingrese la palabra: ")
c = 0

for x in t:
    if x == " ":
        c = c + 1

c = c + 1
print(f"La cantidad de palabras son: {c}")
'''
t = input("Ingrese la palabra: ")
p = t.split()
c = len(p)
print (f"La cantidad de caracteres es: {c}")
