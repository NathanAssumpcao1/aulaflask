x = int(input("Digite valor d x: "))
y = int(input("Digite valor d y: "))
z = int(input("Digite valor d z: "))

if x > y and x > z:
    result  = "x é o maior número"
elif y > x and y > z:
    result  = "y é o maior número"
elif z > x and z > y:
    result  = "z é o maior número"
else:
    result  = "há numeros iguais"
    
print(result)