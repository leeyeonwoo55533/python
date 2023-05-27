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
    n1=[]
    n2=[]
    n3=0
    n4=0
    g1=[]
    li=[]
    for u in d:
        p.append(u)


    for i in range(1,int(max(d))+1):
        n1.append(i)
        if d.count(str(i))==6:
            print(2, i)
            a.append(i)
            while str(i) in d:
                d.remove(str(i))

        else:
            while str(i) in d:
                print(3, i)
                d.remove(str(i))
                e.append(i)


    for x in e:
        while str(x) in p:
            p.remove(str(x))
            print(p)
    for v in e:
        print('v',v)
        if v in n1:
            n1.remove(v)
        else:
            continue
    print(1, n1)
    k={}
    for t1 in range(len(n1)):
        k[n1[t1]] = 0
    print("k",k)
    li=p
    for m in range(len(p)):

        z+=1
        k[n1[t1]] += z
        g1.append(n1[t1])
        li.remove(n1[t1])
    if g1.count(n1[t1]) > 3:
        print("1111111",li)
        continue

    for j in li:
        if j in n2:
            continue

        else:
            n2.append(j)
            print("li의 값",n2,li)

        #o.append(k)
        print(k)

    # for w in range(len(p)):
    #     if k:
    #         continue
