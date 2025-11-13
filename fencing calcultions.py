#12/11/25
#Fence cost calculator
#welcome
#set input for measurments
#set input for cost of fencing per square meter
# all units are in meters

#Version 1.0
def welcome_programme(): #Friendly program to make the user feel welcome. Also makes the program feel a bit more human
    keep_going = True
    while keep_going == True:
        name = str(input("Hi, what is your name? "))
        print(f"Hi {name}, this is a cost calculator for your fence space")
        keep_going = False

def measurement_input_system(question,low): # This function with the 'low' allows us to ask the user any question and the lowest possible eligable awnser is mentioned when the function is called
    error = "Sorry that is not a valid number which is above 0"
    done = False
    while done== False:
        try:
            response = float(input(question))# This response must be a float
            if low< response:
                break

            else:
                print(f"{error}")
        
        except ValueError: #Value error is when the input is given and not the designated type of variable e.g. float
            print(f"{error}")
        
    return response# The return response makes the variable have a value
#This is important as when adding and multiplying variables they ned values or else the 'nonetype' error will occur
    
welcome_programme()
keep_going =""
while keep_going == "":
    width = measurement_input_system(" Hi,please enter a number above 0 for your fence width (Unit in meters) " ,0)
    length = measurement_input_system("Hi, please enter a number above 0 for your fence length (Unit in meters) " ,0)
    cost_per_square_m = measurement_input_system("Hi, please enter a cost for your fencing space, this cost is per meter." ,0)
    #The calling of the funtions above have different questions and also have the 'low.
    perimeter = 2 * (width + length) #perimeter is measurement of the outside lines ( width + width + length + length)
    cost = (perimeter * cost_per_square_m)# cost is perimeter multiplied by cost per square meter
    print(f"The perimeter of your fence space is {perimeter}")
    print(f"Therefore the final cost of your fenced space is {cost}, as {cost_per_square_m} multiplied by {perimeter} results in the final price")
    keep_going = input("Press <ENTER> if you want to continue, or any other key to quit")
    #keep_going is a variable which  is equal to a space. Then the variable is equal to the input. If the user presses <ENTER> then keep_going is still a space. If anything else it isn't a space and the progamm stops looping
print("Thank you for your time, see you next time :)")
