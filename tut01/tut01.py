
def factorial(x):
    if x==1 or x==0:
        print("1")
    else:
        a=1
        for i in range (1,x+1):
            a=a*i
    print(a)
x=int(input("Enter the number whose factorial is to be found "))
factorial(x)
