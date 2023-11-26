#!/usr/bin/env python3

def admin_login(username, password):
    if (username.upper() == "ADMIN" and password == "12345"):
        return "Access granted"
    else:
        return "Access denied"

    # your code here
    #pass

def hows_the_weather(temperature):
    if temperature < 40: 
        return "It's brisk out there!" 
    elif temperature > 40 and temperature <65:
        return "It's a little chilly out there!"
    elif temperature > 85:
        return "It's too dang hot out there!"
    else:
        return "It's perfect out there!"            
    # your code here
    # pass

def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 5== 0:
        return "Buzz"
    elif num % 3 == 0:
        return "Fizz"  
    else:
        return num          
    # your code here
    #pass

def calculator(operation, num1, num2):
    if operation == "+":
        num = num1 + num2
        return num
    elif operation == "-":
        num = num1 - num2
        return num
    elif operation == "*":
        num = num1 * num2
        return num
    elif operation == "/":
        if num2 !=0: #this will avoid dividing a number by 0(zero)
            num = num1/num2
            return num  
        else :
            print("Cannot divide by zero!")
            return None
    else :
        print("Invalid operation!")  
        return None      
    # your code here
    #pass
