# Creating an input system for our coffee program
# Author: Asher Brown
# 17-10-25

#Version 1.0

#TODO:Ask the user fi they like coffee
#      Record the answer
#    Give a response back to the answer

# Ask the user whether they like coffee or not
'''like_coffee= input("Do you like coffee? ")
print(f'Your answer was "{like_coffee}".')

if like_coffee == "yes" or "Yes" or "y" or "Y":
    print("That is great! I like coffee too.")

else:
    print("You are missing out! Why not give it a try?")'''

#Version 2.0
# While loop
'''keep_going=""
while keep_going =="":
    like_coffee= input("Do you like coffee? ")
    if like_coffee == "yes" or like_coffee== "Yes" or like_coffee== "y" or like_coffee=="Y":
        print("That is great! I like coffee too.")
        keep_going= "finished"

    elif like_coffee=="no" or like_coffee=="No" or like_coffee=="n" or like_coffee== "N":
        print("You are missing out! Why not give it a try?")
        keep_going="finished"
    
    else:
        print("Sorry I dont understand")'''
#Version 3
# make programme more pythonic
keep_going =""
while keep_going =="":
    #Convert answer to lowercase using .lower
    like_coffee = input("Do you like coffee? \n").lower()
    print(like_coffee)
    if like_coffee == "yes" or  like_coffee == "y":
        print("That's great! I like coffee too!")
        
    elif like_coffee == "no" or like_coffee == "n":
        print("You are missing out! why not give it a try?")
      
        like_tea=input("Do you like tea instead? \n").upper()
        if like_tea == "YES" or like_tea == "Y":
            print("Good for you. Give coffee a try:)")
        
        
        elif like_tea == "NO" or like_tea == "N":
            print ("I am sorry. That is all I have for now")

        else:
            print("I am sorry I dont understand. Please answe with only yes or no")

    else:
        print("I am sorry I dont understand. Please answe with only yes or no")
   
    keep_going = input("Press <ENTER> to continue, or any other key to quit. Thanks")