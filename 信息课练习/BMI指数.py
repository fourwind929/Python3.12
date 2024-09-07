x=input("请输入您的性别")
if x=="男":
    h=float(input("请输入您的身高(米)"))
    w=float(input("请输入您的体重（kg）"))
    z=w/h**2
    z=round(z,1)

    if z<=16.4:
        print("低体重")
    if 16.5<=z<=23.2:
        print("正常")
    if 23.2<=z<26.3:
        print("超重")
    if z>=26.4:
        print("肥胖")
    
if x=="女":
    h=float(input("请输入您的身高(米)"))
    w=float(input("请输入您的体重（kg）"))
    z=w/h**2
    z=round(z,2)
    
    if z<=16.4:
        print("低体重")
    if 16.5<=z<=22.7:
        print("正常")
    if 22.8<=z<25.2:
        print("超重")
    if z>=25.3:
        print("肥胖")
    


 
