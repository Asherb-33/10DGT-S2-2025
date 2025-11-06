#29/10/25
#area and perimeter calculator
# author: Asher Brown
#Version 1.0

def welcome_programme():
    keep_going = True
    while keep_going == True:
        name = str(input("Hi, what is your name? "))
        print(f"Hi {name}, this is a perimeter and area calculator for a fence space")
        keep_going = False

def measurement_input_system(question,low):
    error = "Sorry that is not a valid number which is above 0"
    done = False
    while done== False:
        try:
            response = float(input(question))
            if low< response:
                break

            else:
                print(f"{error}")
        
        except ValueError:
            print(f"{error}")
        
    return response
    
welcome_programme()
keep_going =""
while keep_going == "":
    width = measurement_input_system(" Hi,please enter a number above 0 for your fence width " ,0)
    length = measurement_input_system("Hi, please enter a number above 0 for your fence length " ,0)
    perimeter = 2 * (length + width)
    area = (length * width)
    print(f"The area of your fence space is {area}")
    print(f"The perimeter of your fence space is {perimeter} ")
    keep_going = input("Press <ENTER> if you want to continue, or any other key to quit")
print("Thank you for your time, see you next time :)")

