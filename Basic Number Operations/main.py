import prime_operation,factorial_operation,armstrong_operation,fibonacci_operation

if __name__=="__main__":
	while True:
		print()
		print("CHOICES")
		print("1. Check a number is prime or not.")
		print("2. Print prime numbers upto n.")
		print("3. Print first n prime numbers.")
		print("4. Print nth prime number.")
		print("5. Print prime number pyramid.")
		print("6. Print factorial of a number")
		print("7. Print total number of permutations.")
		print("8. Print total number of combinations.")
		print("9. Calculate sum of series.")
		print("10. Check a number is armstrong or not.")
		print("11. Print armstrong number upto n.")
		print("12. Print first n armstrong numbers.")
		print("13. Print nth armstrong number.")
		print("14. Print armstrong number pyramid.")
		print("15. Print fibonacci numbers upto n.")
		print("16. Print first n fibonacci numbers.")
		print("17. Print nth fibonacci number.")
		print("18. Print fibonacci number pyramid. ")
		print("19. Exit.")
		
		choice=int(input("Enter your choice : "))
		if choice==1:
			n=int(input("Enter number : "))
			prime_operation.is_prime(n)
		elif choice==2:
			n=int(input("Enter value of n : "))
			prime_operation.prime_upto_n(n)
		elif choice==3:
			n=int(input("Enter value of n : "))
			prime_operation.first_n_prime(n)
		elif choice==4:
			n=int(input("Enter value of n  : "))
			prime_operation.nth_prime(n)
		elif choice==5:
			n=int(input("Enter number of lines : "))
			prime_operation.prime_pyramid(n)
		elif choice==6:
			n=int(input("Enter number : "))
			factorial_operation.print_factorial(n)
		elif choice==7:
			n=int(input("Enter value of n: "))
			r=int(input("Enter value of r: "))
			factorial_operation.permutation(n,r)
		elif choice==8:
			n=int(input("Enter value of n: "))
			r=int(input("Enter value of r: "))
			factorial_operation.combination(n,r)
		elif choice==9:
			n=int(input("Enter number of terms : "))
			factorial_operation.sum_of_series(n)
		elif choice==10:
			n=int(input("Enter number : "))
			armstrong_operation.is_armstrong(n)
		elif choice==11:
			n=int(input("Enter value of n : "))
			armstrong_operation.armstrong_upto_n(n)
		elif choice==12:
			n=int(input("Enter value of n : "))
			armstrong_operation.first_n_armstrong(n)
		elif choice==13:
			n=int(input("Enter value of n : "))
			armstrong_operation.nth_armstrong(n)
		elif choice==14:
			n=int(input("Enter number of lines : "))
			armstrong_operation.armstrong_pyramid(n)
		elif choice==15:
			n=int(input("Enter value of n : "))
			fibonacci_operation.fibonacci_upto_n(n)
		elif choice==16:
			n=int(input("Enter value of n : "))
			fibonacci_operation.first_n_fibonacci(n)
		elif choice==17:
			n=int(input("Enter value of n : "))
			fibonacci_operation.nth_fibonacci(n)
		elif choice==18:
			n=int(input("Enter number of lines : "))
			fibonacci_operation.fibonacci_pyramid(n)
		elif choice==19:
			break
		else: 
			print("Wrong Choice !")
			
			
			
			