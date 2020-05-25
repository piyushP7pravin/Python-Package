def check_armstrong(n):
	tp=n
	no_digit=0
	while tp>0:
		tp//=10
		no_digit+=1
	temp=n
	sum=0
	while temp>0:
		dig=temp%10
		sum+=dig**no_digit
		temp//=10
	if sum==n:
		return True
	else:
		return False