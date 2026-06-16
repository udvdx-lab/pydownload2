c=0

# t_n = 5
s=0

cc =1
while True:
    for z in range(1,cc+1):
        s+=z
    # print(s)

    for x in range(1,s+1):
        if s%x==0:
            c+=1
    # print(c)

    if (c)>500:
        print(s)
        break

    c=0
    s=0
    x=0
    z=0
    cc+=1
