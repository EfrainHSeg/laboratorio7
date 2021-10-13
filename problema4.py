numeropares=0
numeroimpares=0
suma=0
for i in range(6):
    numero=int(input("ingrese un numero: "))
    if numero % 2 == 0:
        numeropares+=1
    else:
            numeroimpares+=1

print("la cantidad de numeros pares es: " , numeropares)
print("la cantidad de numeros impares es: " , numeroimpares)


