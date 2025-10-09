# Creating an input system for our coffee program
# Author: Asher Brown
# 10-10-25

#Version 1.0

#TODO:Ask the user fi they like coffee
#      Record the answer
#    Give a response back to the answer

# Ask the user whether they like coffee or not
like_coffee= input("Do you like coffee? ")
print(f'Your answer was "{like_coffee}".')

if like_coffee == "yes" or "Yes" or "y" or "Y":
    print("That is great! I like coffee too.")

else:
    print("You are missing out! Why not give it a try?")