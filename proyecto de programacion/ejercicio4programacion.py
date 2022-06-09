
# Ahora, diseñe un programa que dibuje la bandera de inglaterra a una dimensión dada, con Lpara el largo horizontal y H para la altura, siendo ambos valores impares mayores a 2 ymenores a 20. Se utilizará únicamente los carácteres 0 y + para realizar la representación

Largo = int(input("Ingrese el numero de longitud : "))
Ancho = int(input("Ingrese el numero de Ancho : "))
nro_de_columnas_izq = int((Largo-1)/2)
nro_de_columnas_derc =  nro_de_columnas_izq 

fila_top_bot = ""
for columna in range(nro_de_columnas_izq):
    fila_top_bot = fila_top_bot + "0"
fila_top_bot = fila_top_bot + " + "
    
for columna in range(nro_de_columnas_derc):
    fila_top_bot = fila_top_bot + "0"
    
fila_central = ""

for columna in range(Largo):
    fila_central = fila_central + "+"
    
nro_de_filas_super = int ((Ancho-1)/2)
nro_de_filas_infer =nro_de_filas_super

print("'\n")

for fila in range(nro_de_filas_super):
    print(fila_top_bot)
    
print("+++++++++++++++++++")

for fila in range(nro_de_filas_infer):
    print("00000000 + 00000000")
    