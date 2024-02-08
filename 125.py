a=int(input("wwedu"))
n=0
suma=0
if a<=100 and a>=0:
    while n!=a:
        n+=1
        print(n)
        suma=suma+n
else:
    print("He pidhodut")
print(suma)