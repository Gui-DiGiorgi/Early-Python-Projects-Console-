def lottery():
    import random
    global lott
    lott=[]
    while len(lott)!=6:
        a=random.randint(1,60)
        if a not in lott:
            lott+=[a]
    lott.sort()
    
    return lott

def bet():
    global lucky_number
    lucky_number=["first","second","third","fourth","fifth","sixth"]
    n=0
    bet_num=0
    for num in lucky_number:
        bet_num=int(input("Type the "+num+" number of your bet (1 to 60 allowed): "))
        while bet_num>60 or bet_num<1:
            print("This number is not allowed, try another")
            bet_num=int(input("Type the "+num+" number of your bet (1 to 60 allowed): "))
        while bet_num in lucky_number:
            print("You already chose this number, try another")
            bet_num=int(input("Type the "+num+" number of your bet (1 to 60 allowed): "))
        lucky_number[n]=bet_num
        n+=1
    lucky_number.sort()
    
    ans=int(input("Your bet is "+str(lucky_number)+", correct? 1- Yes 2- No "))
    if ans==1:
        return
    else:
        bet()
    


def compare():
    global luck
    luck=0
    comp_test=lott.copy()
    
    for i in lucky_number:
        kill=0
        for j in comp_test:
            if i>=j:
                if i>j:
                    kill+=1
                else:
                    luck+=1
                    kill+=1
                    break
            if j>i:
                break
        
        for j in range(kill):
            comp_test.pop(0)
        if comp_test==[]:
            break
            
    return luck

luck=0
times_all=0
times_4=0
times_5=0
bet()

while luck!=6:
    times_all+=1
    lottery()
    compare()
    if luck==4:
        times_4+=1
    if luck==5:
        times_5+=1
        print("You got 5, in lottery "+str(lott)+"!")
        print("In",times_all,"tries, you got 4:",times_4,"times ("+str(times_4/times_all)+"%) \
and 5:",times_5,"times ("+str(times_5/times_all)+"%)")
          
print("Congratz, after getting 4 numbers", times_4,"times and 5 numbers",times_5,"times, and doing overall",times_all,"tries, you got the full prize, in lottery", lott)
