print("Think of a number from 0 to 1023. I'm going to guess your number.")
a=512
b=0
while a>=1:
    answer=int(input("\nIs your number bigger or equal to "+repr(a+b)+"? Please type the number of your choice below\n1.Yes\n2.No\n"))
    if answer==1:
        b+=a
        a/=2
        a=int(a)
    else:
        a/=2
        a=int(a)
print("\nYour number is "+repr(b))
        
