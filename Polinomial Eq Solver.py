# This script solves the poli equation for 1 of their real solutions, if such exists

def easy_eq(ans,num_list):
    s = 0
    for i,n in zip(num_list,range(len(num_list))):
        s += i*(ans**n)
        
    return s

# expression for z

f=int(input("Type the highest power of x: "))
e=[]
print()
for i in range(0,f+1):
    a=float(input("Please, type the number multiplying x^"+str(i)+": "))
    e+=[a]

x=0
z=-1
t=0
p=1
while z<0 and t<1000:
    x=p
    z=easy_eq(x,e)
    if t%2==0 and z<0:
        p*=-1
    if t%2!=0 and z<0:
        p*=10
    t+=1

t=0
n=1
while z>0 and t<1000:
    x=n
    z=easy_eq(x,e)
    if t%2==0 and z>0:
        n*=-1
    if t%2!=0 and z>0:
        n*=10
    t+=1
    
if z!=0 and t<1000:    
    print("\nThe answer is between {} and {}. \n".format(p,n))

if t==1000:
    if z>0:
        print("It appears that there no negative value for z, so possibly no answer")
    if z<0:
        print("It appears that there no positive value for z, so possibly no answer")
    if z==0:
        print("It appears that the answer is",x)



while abs(z)>1e-12:
    x=(p+n)/2
    z=easy_eq(x,e)
    if z>0 and abs(n-p)>abs(n-x):
        p=x
    if z<0 and abs(n-p)>abs(x-p):
        n=x
        
if z!=0:
    print("One real value for x is approximately",x)

else:
    print("One real value for x is",x)
    
