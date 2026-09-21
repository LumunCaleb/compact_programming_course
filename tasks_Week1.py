#TASK1
from math import factorial, pi 
# Press the green button in the gutter to run the script. 
if __name__ == '__main__': 
    r = float(input("Input the radius of the circle : "))
    print("### TASK1 ###")
    print("The area of the circle with radius " + str(r) + " is: " + str(pi * r ** 2))

#TASK2
print("### TASK2 ###")
#Step1: Creating variables of differemt types with values assigned to them
zahl = 10 #Creaiting an int variable and assigning it a value of 10
kommazahl = 10.5 #Creating a float variable and assigning it a value of 10.5
text = "Hello World" #Creating a string variable and assigning it a value of "Hello World"
wahrheitswert = True #Creating a boolean variable and assigning it a value of True

#Step2: Printing the values of the variables to the console
print("Integer value: ", zahl)
print("Float value: ", kommazahl)   
print("String value: ", text)
print("Boolean value: ", wahrheitswert)

#Step3: Printing the variable types to the console
print("Type of value" + str(zahl) + "is:", type(zahl))
print("Type of value" +str(kommazahl) + "is:", type(kommazahl))
print("Type of value" + str(text), type(text))
print("Type of value" + str(wahrheitswert), type(wahrheitswert))

#TASK3
print("### TASK3 ###")
#Converting the created Variables to different types and printing the values and types

#Converting the integer variable to float
print("Converted", zahl, "from int to float:", float(zahl))

kommazahl = int(kommazahl) #Converting the float variable to integer
print("Converted", kommazahl, "from float to int:", kommazahl)

kommazahl = str(kommazahl) #Converting the integer variable to string
print("Converted", kommazahl, "from int to string:", kommazahl)

#Converting the string variable with integer to an integer
print("Converted" + str("55") + "from string to int:", int("55"))

int_to_bool  = bool(zahl)
print("Converted Integer ", zahl, "to Boolean: ", int_to_bool)

#TASK4
print("### TASK4 ###")
#Option1: Using a while loop
factorial_number = int(r)    #Converting the factorial number to the inputed radius
number = factorial_number
factorial_new = 1

while number !=0:
    factorial_new = factorial_new * number 
    number -=1

print("The factorial of " + str(factorial_number) + " is: " + str(factorial_new))

#Option2: Using the math.factorial function
factorial_new = factorial(int(r)) 
print("The factorial of " + str(factorial_number) + " is: " + str(factorial_new))

#Option 2 is more efficient and faster than option 1. 
#It is also more readable and easier to understand. It is also less prone to errors.