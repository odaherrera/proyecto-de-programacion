#PROBLEMA1
#Datos registrados en la salida de campo

n = int(input('ingrese un número total de dias que duro la salida campo: '))

#dias con variaciones de error

dias_variaciones = int(input('ingrese dias con variaciones de error (coloque 0 para terminar): ')) 

dias_variaciones1 = []
while dias_variaciones > 0:
  
    #agregamos dias con variaciones de error en la lista
    dias_variaciones1.append (dias_variaciones)
    #pedimos un nuevo valor a la lista
    dias_variaciones = int(input('ingrese dias con variaciones de error (coloque 0 para terminar): '))

#ordenando los dias de variacion de mayor a menor
dias_variaciones1.sort (reverse=True)
#cantidad de dias con variaciones 
total_dias_variacion = len(dias_variaciones1 )

mayor_100 = []
menor_100 = []
#valores mayores y menores a 100 de los dias
for i in range(len(dias_variaciones1)):
    if dias_variaciones1[i] < 100:
        mayor_100.append (dias_variaciones1[i])
    elif dias_variaciones1[i] > 100:  
        menor_100.append (dias_variaciones1[i])

#media de los valores
suma = 0
for i in range(len(dias_variaciones1)):
    suma = suma + dias_variaciones1[i]

dias_sin_variacion = n - suma

varianza_max = 0
for i in range(len(mayor_100)):
    varianza_max1 = (mayor_100[i]-suma)**2
    varianza_max = varianza_max + varianza_max1 

varianza_max_total =  varianza_max/dias_sin_variacion

varianza_min = 0
for i in range(len(menor_100)):
    varianza_min1 = (menor_100[i]-suma)**2
    varianza_min = varianza_min + varianza_min1 

varianza_min_total =  varianza_min/dias_sin_variacion

print ('el numero de dias totales que duro la salida de campo es:',n)
print ('los dias con variaciones fueron: ',dias_variaciones1)
print ('los dias totales con variaicones fueron: ',total_dias_variacion)
print ('valores mayores a 100: ',mayor_100)
print ('valores menores a 100: ',menor_100)
print ('la variacion maxima es: ', varianza_max_total)
print ('la variacion minima es: ', varianza_min_total)

