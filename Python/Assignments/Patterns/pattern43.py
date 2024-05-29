n=int(input("Enter the number of lines : "))
for i in range(0,n):
	for j in range(n,0,-1):
		if j>i:
			print("*",end=" ")
		else:
			print(" ",end=" ")
	for k in range(0,n+1):
		if k>i:
			print("*",end=" ")
		else:
			print(" ",end=" ")
	print(" ")
