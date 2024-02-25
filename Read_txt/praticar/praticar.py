"o usuario vai digitar 10 numeros e depois mostre quantas desses numeros sao numeros possitivos ,negativos e zero"
lista=[]
possitivos=0
negativos=0
zero=0
for c in range(3):
    print(f"digite {3-c}numeros:")
    x=int(input())
    lista.insert(c,x)
    if (x>0):
        possitivos+=1
    elif (x<0):
        negativos+=1
    else:
        zero+=1
# print(f"os numeros digitados sao : "+ lista)
print(f"os nmeros positivos sao :{possitivos}")
print(f"os nmeros positivos sao :{negativos}")
print(f"os nmeros positivos sao :{zero}")

