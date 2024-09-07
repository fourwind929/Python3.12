x=float(input())
if x<=1:
    print("15")
else:
    if x%1==0:
        z=15+10*(x-1)
        
        if z>=100:
            c=0.9*z
            print(c)
        else:
            print(z)
    else:
        y=15+(10*(x//1))
        
        if y>=100:
            c=0.9*y
            print(c)
        else:
            print(y)


 
