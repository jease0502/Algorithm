def findsmall(arr):
	small=arr[0]
	small_index=0
	for i in range(1,len(arr)):
		if arr[i]<small:
			small_index=i
	return small_index

def select(arr):
	newarr=[]
	for i in range(len(arr)):
		small=findsmall(arr)
		newarr.append(arr.pop(small)) #這邊的small是上面的small_index，這邊沒有全域宣告\
	return newarr

print(select([5,3,6,2,10,15]))
