b=input("Enter hours: ")
c=input("Enter rate :")
x= int(b)
y= int(c)
def hourly_rate(x,y):
    if x > 40:
        z=((x-40)/2)*y+(40*y)
        print ("Your pay is: ",z)
    else:
        a=x*y
        print ("Your pay is: ",a)
hourly_rate(x,y)
