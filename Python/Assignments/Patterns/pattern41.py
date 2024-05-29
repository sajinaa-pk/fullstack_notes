n=int(input("enter the maximum count : "))
for x in range(n,0,-1):
	for i in range(1,x+1):
		for j in range(1,i+1):
			print(j,end=" ")
		print("")
	for i in range(x-1,1,-1):
		for j in range(1,i+1):
			print(j,end=" ")
		print("")
print(x)