def func(arr,k):
	if k in arr:
		return True
	else:
		return False

n=int(input("enter number of elements"))
arr=[]
for i in range(0,n):
	ele=int(input())
	arr.append(ele)
k=int(input("enter search element"))
print(func(arr,k))

