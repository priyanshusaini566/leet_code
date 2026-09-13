s="RLRRLLRLRL"

l=list(s)
balance=0
count=0

for i in range(len(l)):
    if l[i]=='R':
        balance+=1

    elif l[i]=='L':
        balance-=1

    if balance==0:
        count+=1

print(count)

