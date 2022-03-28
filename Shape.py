def perirectangle(x,y):
    return x+x+y+y

def areaofrectangle(x,y):
    return x*y

def areaofsquare(x):
    return x**2

if __name__ == "__main__":

    while(True):
        print('''
                 1. Area of rectangle
                 2. Perimeter of Rectangle
                 3. Area of Square
                 ''')
        ch = int(input("Select an option : "))

        if(ch==1):
            x = int(input("Enter a : "))
            y = int(input("Enter b : "))
            perirectangle(x,y)
        elif(ch==2):
            x = int(input("Enter a : "))
            y = int(input("Enter b : "))
            areaofrectangle(x, y)
        elif(ch==3):
            x = int(input("Enter side : "))
            areaofsquare(x)
        else:
            print("Invalid Number")










