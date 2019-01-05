f=0
kel=0

def c2f(temp):
    global f
    f=(temp*9/5)+32
    print(f)

def c2k(temp):
    global kel
    kel=temp+273
    print(kel)

def tempmenu():
    print("1.Enter new temperature (Celsius)")
    print("2.Celsius to Farenheit")
    print("3.Celsius to Kelvin")
    print("4.Display")
    print("5.Exit")
   
    while 1:
        print("enter choice")
        ch=int(input())
        if(ch==1):
            print("Enter temperature (Celsius)")
            temp=int(input())
        elif(ch==2):
            c2f(temp)
        elif(ch==3):
            c2k(temp)
        elif(ch==4):
            a=["the temp in C:",temp,"to F is",f,"the temp in K is",kel]
            print(a)
        elif(ch==5):
            print("Program terminated successfully")
            exit()
        else:
            print("Invalid Option")

tempmenu() 
