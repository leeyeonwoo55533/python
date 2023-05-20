# python
#9017-크로스 컨트리
#9017-크로스 컨트리
t=int(input())
c=0

for i in range(t):
    n = int(input())
    d = input().split()
    p = []
    a = []
    e = []
    z=0
    o=[]
    for u in d:
        p.append(u)

    for i in range(1,int(max(d))+1):

        if d.count(str(i))==6:
            a.append(i)
            while str(i) in d:
                d.remove(str(i))
        else:
            while str(i) in d:
                d.remove(str(i))
                e.append(i)

    for x in e:
        while str(x) in p:
            p.remove(str(x))
            print(p)
    for m in range(len(p)):
        z+=1
        k={p[m]:z}
        o.append(k)
    print(o)
    # for y in range(len(a)):

