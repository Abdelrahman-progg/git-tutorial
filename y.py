l= input()
s=list(input())
lst=list('qwertyuiopasdfghjkl;zxcvbnm,./')
for i in range(len(s)):
    if l=='R':
        s[i]=lst[lst.index(s[i])-1]
    else:
        s[i]=lst[lst.index(s[i])+1]
# for i in range(l):
#     print(s[i],)
print(''.join(s))