n=int(input("Enter the count : "))
for i in range(n,0,-1):
	for j in range(n,i-1,-1):
		print(j, end=" ")
	print()
for i in range(2,n+1):
	for j in range(n,i-1,-1):
		print(j, end=" ")
	print()

