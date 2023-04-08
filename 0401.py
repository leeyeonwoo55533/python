# a=input().split()
# c=[]
#
# b=int(a[0])
# d=int(a[1])
# for i in range(1,b+1):
#     if  b % i == 0:
#         c.append(i)
#     else:
#         continue
#
# if len(c)-d<0:
#     print(0)
# else:
#     print(c[d-1])


#2309
# a=[]
# b=0
# for i in range(9):
#     a.append(int(input()))
#     b+=a[i]
#
# c=b-100
# d=0
# e=0
#
# a=sorted(a)
#
# for j in range(9):
#     if c-a[j] in a:
#         d+=(a[j])
#         e+=(c-a[j])
#         break
#     else:
#         continue
#
# a.remove(d)
# a.remove(e)
#
# for x in range(len(a)):
#     print(a[x])

#2609

# a=input().split()
#
# b=int(a[0])
# c=int(a[1])
# d=[]
# e=[]
# q=0
# t=0
#
# for i in range(1,b+1):
#     if b % i==0:
#         d.append(i)
#     else:
#         continue
#
#
# for j in range(1,c+1):
#     if c % j==0:
#         e.append(j)
#     else:
#         continue
#
#
# for x in e[::-1]:
#     if x in d:
#         q=x
#         break
#     else:
#         continue
#
# print(q)
#
# t=(c*b)
#
# print(t//q)


a=int(input())
b=int(input())
c=input().split()
c.sort()
d=0
e=0



for i in c:
    e=str(b-int(i))
    if e in c:
        d+=1
        c.remove(i)
        c.remove(e)


print(d)








