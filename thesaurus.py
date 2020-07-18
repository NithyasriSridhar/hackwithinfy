n=int(input())
for i in range(n):
    s=input()
    if s[0]==s[len(s)-1]:
        k=set()
        if "?" not in s:
            print(1)
        for a in s:
            if a=='?':
                continue
            k.add(a)
        else:
            print(26-len(k))
    else:
        if s[len(s)-1]=="?" or s[0]=="?":
            print(1)
        else:
            print(0)
