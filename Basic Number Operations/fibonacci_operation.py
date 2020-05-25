import fibonacci

def fibonacci_upto_n(n):
	for i in range(1,n+1):
		if fibonacci.nth_fibonacci(i)<n+1:
			print(fibonacci.nth_fibonacci(i),end=" ")

def first_n_fibonacci(n):
	for i in range(1,n+1):
		print(fibonacci.nth_fibonacci(i),end=" ")
		
def nth_fibonacci(n):
	print(fibonacci.nth_fibonacci(n),end=" ")

def fibonacci_pyramid(n):
	a=1
	for i in range (1,n+1):
		for j in range(i,n):
			print(end=" ")
		for j in range(1,i+1):
			print(fibonacci.nth_fibonacci(a),end=" ")
			a+=1
		print()


			


