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
    count=0

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
                e.append(i)#list e 는 팀원 수가 6명가 아닌 팀


    for x in e:
        while str(x) in p:# list p 는 팀원 수가 6명인 팀
            p.remove(str(x))
            print(p)
    for v in e:
        print('v',v)
        if v in n1:
            n1.remove(v)
        else:
            continue
    print("n1:", n1)

    for count in range(len(n1)):
        o.append([])

    for count2 in p:
        for count3 in range(len(n1)):
            print(count2, count3)
            if int(count2)==n1[count3]:
                o[count3].append(count)
                count+=1
                continue
            print(o)

