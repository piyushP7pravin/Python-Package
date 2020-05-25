import factorial

def print_factorial(n):
	fact=factorial.factorial(n)
	print(fact)

def permutation(n,r):
	fact_n=factorial.factorial(n)
	fact_n_r=factorial.factorial(r)
	print(fact_n//fact_n_r)

def combination(n,r):
	fact_n=factorial.factorial(n)
	fact_r=factorial.factorial(r)
	fact_n_r=factorial.factorial(n-r)
	print(fact_n//(fact_n_r*fact_r))

def sum_of_series(n):
	sum=0
	if n%2==0:
		for i in range(0,n+1):
			sum+=1/factorial.factorial(2*i)
		print(sum)
	else:
		for i in range(0,n+1):
			sum+=1/factorial.factorial(i+1)
		print(sum)
		