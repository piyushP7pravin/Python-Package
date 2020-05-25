import armstrong

def is_armstrong(n):
	if armstrong.check_armstrong(n)==True:
		print("Armstrong Number")
	else:
		print("Not Armstrong Number")

def armstrong_upto_n(n):
	for i in range(1,n+1):
		if armstrong.check_armstrong(i)==True:
			print(i,end=" ")

def first_n_armstrong(n):
	a=1
	count=1
	while count<n+1:
		if armstrong.check_armstrong(a)==True:
			print(a,end=" ")
			count+=1
		a+=1

def nth_armstrong(n):
	a=1
	count=1
	while count<n+1:
		if armstrong.check_armstrong(a)==True:
			count+=1
		a+=1
	print(a-1)
	
def armstrong_pyramid(n):
	a=1
	for i in range(1,n+1):
		for j in range(i,n):
			print(end=" ")
		for j in range(1,i+1):
			count=1
			while count==1:
				if armstrong.check_armstrong(a)==True:
					print(a,end=" ")
					count+=1
				a+=1
		print()
			
	