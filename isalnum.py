s="3[a]2[bc]"

s1=""

for i in range(len(s)):
    if s[i].isdigit():
        num=int(s[i])
        i+=2
        word=""

        while s[i]!=']':
            word=word+s[i]
            i+=1

        s1=s1+word*num

print(s1)