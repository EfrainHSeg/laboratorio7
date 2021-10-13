pares=0
impares=0
positivos=0
negativos =0
neutros=0
limite= int(input("ingrese el limite: "))
for i in range(limite):
    if i % 2 == 0:
        pares +=1
    else:
        impares +=1
       

    if i< 0 :
        negativos +=1
    
    else:
        positivos +=1
    if 1 == 0:
        neutros +=1
        

print(" cantidad de numeros pares : " , pares)
print("cantidad de numeros impares : " , impares)
print(" cantidad de numeros negativos : " , negativos)
print(" cantidad de numeros positivos : " , positivos)
print("cantidad de numeros neutros: " , neutros)
