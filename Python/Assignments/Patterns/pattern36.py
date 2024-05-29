n=int(input("Enter the count : "))
for i in range(n,0,-1):
	for j in range(1,n+1):
		if j>=i:
			print(j,end=" ")
		else:
			print(" ",end=" ")
	print()

