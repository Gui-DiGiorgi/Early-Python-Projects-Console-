# Calculator

def instructions():
	print("\nHello, welcome, before using it, please, read the instructions:")
	print("This calculator has 4 main functions abbreviated as follows:")
    
	print("1.Add - Addition, 2.Sub - Subtraction, 3.Mul - Multiplication e 4.Div - Division")
	print("Extra Functions 1.C - Clear, 2.Str - Store e 3.Rec - Recover, with 4 SS - Storage Space")
	print("Instr - Instructions")
	print("A - Answer")
	print("Please, press the button when asked to")

# Variáveis:

# num1 - Primary Number, num2 - Secundary Number

def add(num1):
	num2=float(input("\nType the numbers that will add to "+str(num1)+": "))
	num1+=num2
	return num1

def sub(num1):
	num2=float(input("\nType the numbers that will sub to "+str(num1)+": "))
	num1-=num2
	return num1

def mul(num1):
	num2=float(input("\nType the numbers that will mul to "+str(num1)+": "))
	num1*=num2
	return num1

def div(num1,num2):
	num1/=num2
	return num1

# SS1-4 - Storage Space 1 to 4
		
# Recover:

def recover():
	while 1==1:
		recover=int(input("\nRecover a value: 1.SS1("+str(ss1)+") 2.SS2("+str(ss2)+") 3.SS3("+str(ss3)+") 4.SS4("+str(ss4)+") "))
		if recover==1:
			num1=ss1
			break
		elif recover==2:
			num1=ss2
			break
		elif recover==3:
			num1=ss3
			break
		elif recover==4:
			num1=ss4
			break
		else:
			print("\nPlease, type a valid input")
	return num1

instructions()

turned_on=int(input("\nDo you want to use the calculator? Type a number: 1.Yes 2.No "))

ss1=0
ss2=0
ss3=0
ss4=0

while turned_on==1:
# a is the answer/number used
	a=float(input("\nType your number: "))
	while 1==1:
		operation=int(input("\nR: "+str(a)+". What do you want to do? 1.Add 2.Sub 3.Mul 4.Div 5.C 6.Sto 7.Rec 8.Instr 9.Exit "))
		if operation == 1:
			a=add(a)
		elif operation == 2:
			a=sub(a)
		elif operation == 3:
			a=mul(a)
		elif operation == 4:

			# Since in divison a/b is not equal b/a, we need to select both a and b for a/b:
			a1=a
			div_choice=int(input("\nDo you wish to use a stored number as divisor? 1.Yes 2.No "))		
			a2=0
			print("\nPlease, don't try 0")
			while a2==0:
				if div_choice==1:
					a2=recover()
					if a2==0:
						div_choice=int(input("\nDon't use 0. Try: 1. Stored Number 2. New Number "))
				elif div_choice==2:
					a2=float(input("\nType the divisor: "))
					if a2==0:
						div_choice=int(input("\nDon't use 0. Try: 1. Stored Number 2. New Number "))
				else:
					print("\nUse a valid input")
					div_choice=int(input("\nDo you wish to use a stored number as divisor? 1.Yes 2.No "))

			a=div(a1,a2)


		elif operation == 5:
			a=float(input("\nType your number: "))
		elif operation == 6:
			# armazenar:
			while 1==1:
				space=int(input("\nWhat Space? 1.SS1("+str(ss1)+") 2.SS2("+str(ss2)+") 3.SS3("+str(ss3)+") 4.SS4("+str(ss4)+") "))
				if space==1:
					ss1=a
					break
				elif space==2:
					ss2=a
					break
				elif space==3:
					ss3=a
					break
				elif space==4:
					ss4=a
					break
				else:
					print("\nUse a valid input")

		elif operation == 7:
			a=recover()
		elif operation == 8:
			instructions()
		elif operation == 9:
			print("\nThanks for using it")
			turned_on=2
			break
		else:
			print("\nUse a valid input")
print("\nBye")
