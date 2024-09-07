n=int(input("饮品种类是"))
min=int(input("该饮品销量为"))
for i in range(n-1):
    x=int(input("该饮品销量为"))
    if x<min:
        min=x
print("销量最少的为",min)
 
