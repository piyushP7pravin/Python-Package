import prime

def is_prime(n):
	if prime.check_prime(n)==True:
		print("Prime Number")
	else:
		print("Not Prime")
		
def prime_upto_n(n):
	for i in range(1,n+1):
		if i>1:
			if prime.check_prime(i)==True:
				print(i,end=" ")
			
def first_n_prime(n):
	a=1
	count=1
	while count<n+1:
		if prime.check_prime(a)==True:
			print(a,end=" ")
			count+=1
		a+=1

def prime_pyramid(n):
	a=2
	for i in range(1,n+1):
		for j in range(i,n):
			print(end=" ")
		for j in range(1,i+1):
			count=1
			while count==1:
				if prime.check_prime(a)==True:
					print(a,end=" ")
					count+=1
				a+=1
		print()
		
def nth_prime(n):
	a=2
	count=1
	while count<n+1:
		if prime.check_prime(a)==True:
			count+=1
		a+=1
	print(a-1)
		
			
			