def sum(list):
	if list == []:
		return 0
	return list[0]+sum(list[1:])
list=[]
z=eval(input("請輸入幾位數相加"))
for x in range(z):
	y=eval(input())
	list.append(y)
print(sum(list))
