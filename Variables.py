#demonstrate how variable are created and how they work
#Author: Asher Brown
#Date: 08-10-2025
#v1.1

#Different types pf variables
#store a string
greeting="Hello World!"
print (greeting)

#store a number
my_number = 80
print(my_number)

my_number2 = 7
print(my_number2) 

#Assign the value of one variable to another
my_number = greeting
print(my_number) # do not assign value to variables that do not make sense
'''Do calculations with variables and store the results
 in another variable. I can now 
 press enter
 as many times
 as 
 I like '''

# creating new variable
num_1 = 5
num_2 = 18
sum_1 = num_1 + num_2
print(sum_1)

#concatination:
sum_string1="18"
sum_string2="5"
stringsum=sum_string1+sum_string2
print(stringsum)

#print formating
print(f"My calculation for adding {num_1} and {num_2} together is {sum_1}.")
#F stands for format. and insert the value of variables into the curly brackets {}