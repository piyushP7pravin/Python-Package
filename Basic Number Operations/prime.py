def check_prime(n):
	if n>1:
		flag=False
		for i in range(2,n//2+1):
			if n%i==0:
				flag=True
				return False
				break
		if flag==False:
			return True
	else:
		return False
