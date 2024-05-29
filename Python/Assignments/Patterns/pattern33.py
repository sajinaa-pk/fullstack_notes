n=int(input("Enter the limit : "))
for i in range(n,0,-1):
	for j in range(n,0,-1):
		if j<=i:
			print(j,end=" ")
		else:
			print(" ",end=" ")
	print()
for i in range(1,n+1):
	for j in range(n,0,-1):
		if j<=i:
			print(j,end=" ")
		else:
			print(" ",end=" ")
	print()

