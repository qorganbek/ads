def isPrime(n):
	for i in range(2,n):
		if n % i == 0:
			return False
	return True		 


a = int(input())
if isPrime(a):
	print("prime")
else: print("composite")	