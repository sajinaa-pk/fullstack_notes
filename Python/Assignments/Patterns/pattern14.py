n=int(input("Enter the count :"))
for i in range(1,n+1):
	for j in range(1,i+1):
		if j%2==0:
			print("+",end=" ")
		else:
			print("*",end=" ")
	print()
for i in range(n-1,0,-1):
	for j in range(1,i+1):
		if j%2==0:
			print("+",end=" ")
		else:
			print("*",end=" ")
	print()
