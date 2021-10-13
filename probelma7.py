par=0
impar=0
sumarpar=0
sumaimpar=0
limite=int(input("ingrese el limite: "))
for i in range (limite):
    number=int(input("ingrese el numero: "))
    if number%2 ==0:
        par +=number
    else:
        impar +=number
    sumarpar += par
    sumaimpar += impar

print("la suma de los pares es:" , sumarpar) 
print("la suma de los impares es : " , sumaimpar)   

