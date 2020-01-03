# Brute Factor Finder

a = int(input("Please, enter the number to be factored: "))
c = a

b = 2
factors = []
d = 0
p = 0
n = 0

while a!=1:
    if a%b== 0:
        factors+= [b]
        a/= b
        if d!=b:
            n+=1
            d=b
        b=2
        p+=1
    else:
        b+=1
        
if p>1:
    print("\n"+repr(c)+" has",n,"unique factors and it is factored like this:", factors)
else:
    print("\n"+repr(c)+" is prime")
