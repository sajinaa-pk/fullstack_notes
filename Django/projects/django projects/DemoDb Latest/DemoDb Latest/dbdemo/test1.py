list1=["hello",["hi,","how"]]
for i in list1:
	for j in i:
		if "," in j:
			j.replace(",","")
print(list1)