
numbers=[1,2,7,3,4]
target=9
l1=[]
n=len(numbers)
for i in range(n-1):
    for j in range(i+1,n):
        if numbers[i]+numbers[j]==target:
            l1.append(i+1)
            l1.append(j+1)

print(l1)