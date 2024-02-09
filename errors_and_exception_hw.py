#Q! handle the exception thrown by the code  below by using try and exception blocks
try:
    for i in ['a','b','c']:
        print(i**2)
except:
    print("List Item Type Not Supported for Exponential function")
finally:
    print("Done with Try-Exception bock")

print('\n---------------------------------------------------------------------------\n')
#Q! handle the exception thrown by the code  below by using try and exception blocks
x = 5
y = 0

try:
    z = x/y
except:
    print("Error : You are tryin to divide a number by 0")
else:
    print("Divison Done")
finally:
    print('All Done')

print('\n---------------------------------------------------------------------------\n')
#Q3: Write a function that asks for an integer and prints the square of it. 

def ask():
    while True:
        try:
            integer = int(input("Please Enter an Integer : "))
        except:
            print("You have not entered a number please try again")
        else:
            print(integer**2)
            break
        finally:
            print("------")

ask()