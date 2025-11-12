#12/11/25
#Fence cost calculator
#welcome
#set input for measurments
#set input for cost of fencing per square meter
# all units are in meters

#Version 1.0
def welcome_programme():
    keep_going = True
    while keep_going == True:
        name = str(input("Hi, what is your name? "))
        print(f"Hi {name}, this is a cost calculator for your fence space")
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
    width = measurement_input_system(" Hi,please enter a number above 0 for your fence width (Unit in meters) " ,0)
    length = measurement_input_system("Hi, please enter a number above 0 for your fence length (Unit in meters) " ,0)
    cost_per_square_m = measurement_input_system("Hi, please enter a cost for your fencing space, this cost is per meter." ,0)
    perimeter = 2 * (width + length)
    cost = (perimeter * cost_per_square_m)
    print(f"The perimeter of your fence space is {perimeter}")
    print(f"Therefore the final cost of your fenced space is {cost}, as {cost_per_square_m} multiplied by {perimeter} results in the final price")
    keep_going = input("Press <ENTER> if you want to continue, or any other key to quit")
print("Thank you for your time, see you next time :)")