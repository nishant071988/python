try:
    hours= input("Enter hours :")
    rate = input("Enter per hour rate :")
    x=int(hours)
    y=int(rate)
    if x>40:
        z= x-40
        a=(40*y)+(1.5*y)*z
        print ("Toatal pay",a)
    else:
        m=x*y
        print ("Toatal pay",m)
except:
    print ("Wrong value,please try again")
    
