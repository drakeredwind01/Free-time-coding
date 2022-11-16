a=int(input("enter 1 thing: "))
b=int(input("enter 2 thing: "))
c=int(input("enter 3 thing: "))
d=int(input("enter 4 thing: "))
e=int(input("enter 5 thing: "))
f=[a,b,c,d,e]
for g in range (0,5):
    for h in range(0, 5):
        for i in range (0,5):
            for j in range (0,5):
                #for k in range (0,5):
                    if(g!=h&g!=i&g!=j&g!=k&h!=g&h!=i&h!=j&h!=k&i!=g&i!=h&i!=j&i!=k&j!=g&j!=h&j!=i&j!=k&k!=g&k!=h&k!=i&k!=j):
                        print(f[g],f[h],f[i],f[j],f[k])



'''
                    if(g!=h&h!=g&h!=i&h!=j&h!=k&i!=g&i!=h&i!=j&i!=k&j!=g&j!=h&j!=i&j!=k&k!=g&k!=h&k!=i&k!=j):

'''