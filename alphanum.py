s="A man, a plan, a canal: Panama"

s1=""
s=s.lower()

for item in s:
    if item.isalnum():
        s1=s1+item

    else:
        continue

rev=s1[::-1]
if rev==s1:
    print("true")
else:
    print("False")
