def linear_search(a,key):
    n = len(a)
    for i in range(n):
        if a[i] == key:
            return i
    return -1
a=[13,20,28,32,41,50]
print("the array elements are:",a)
k = int(input("enter the key element to search:"))
i = linear_search(a,k)
if i == -1:
    print("search unsuccessful")
else:
    print("search is successful key found at location:",i+1)
