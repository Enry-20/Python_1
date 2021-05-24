string1= "My-boolls"
lista1=[3, 4]
lista2=[2, 1]

#print(dir(string1))
#diversos metodos

print(string1.upper())
#metodo para cambiar letras minusculas a mayusculas
print(string1.swapcase())
#metodo para cambiar letras de minuscula a mayuscula o el contrario
print(string1.replace("My", "your").upper())
#Remplaza el string seleccionado
print(string1.count("o"))
print(string1.startswith("my"))
#metodo que comprueba si un string empieza con determinado valor
print(string1.endswith("boolls"))
print(string1.split("-"))
#corta en 2 el string dependiendo del signo para hacerlo, autamaticamente lo hace si exise un espacio

i= len(string1)
#el metodo "len" sirve para contar el numero de caracteres de una variable y/o agrupacion
i= len(lista2)
print(i)

suma=(lista1[0]+ lista2[1])
print(suma)










