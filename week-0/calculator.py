#the int() is for put a type int (4) and float() is for put a type float (4.2)
#x = float(input("What's x? "))
#y = float(input("What's y? "))

#plus two numbers
#z = x + y

#the round is for round a digit, for example 1.5 + 4.7 = 6,2 round(6)
#z = round(x + y )

#z = x / y

#print(f"{z:.2f}")




def main():
    x = int(input("What's x? "))
    #y = int(input("What's x? "))
    print("x squared is", square(x))
    
def square(n):
    return pow(n, 2)
main()