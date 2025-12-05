#calculator_functions.py 

def add(n1, n2):
    return n1 + n2 

def subtract(n1, n2): 
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

#checks to see if divisor is zero
def divide(n1, n2):
    if n2 == 0:
        return "Error: Cannot divide by zero!"
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

operations_strings = {
    "+": "add",
    "-": "subtract",
    "*": "multiply",
    "/": "divide"
}

#Checks to see if the input can be converted to a float
def check_float_input(float_input):
    try: 
        number = float(float_input) 
        return True 
    except ValueError:  
        return False 
    else: 
        return False 
    
#This while loops checks to see if the input is a float number
def get_float_input():
    while(True):
        float_input = input()
        if (check_float_input(float_input) == True): 
            return float(float_input)
        else: 
            print("The input you gave is not a float number. Try again") 

 #A shortcut for printing all the operators on screen
def print_operators(): 
    print("Choose one of the following operators")
    for symbol in operations:
        print( symbol +',', end=' ') 
    print()
    print("c, (Clear)") 
    print("n, (New Float)")
    print("e, (Exit)")

#checks to see if operator is in Dictionary
def check_operator_input(operator_input): 
    if operator_input in operations: 
        return True 
    else: 
        return False


#Takes input from a user and checks to see if it is a correct operator input option 
def get_operator():  
    while(True):
        operator_input = input() 
        if check_operator_input(operator_input) == True:
            return operator_input  
        elif operator_input == "c" or operator_input == "C": 
            operator_input = "c"
            return operator_input 
        elif operator_input == "n" or operator_input == "N": 
            operator_input = "n"
            return operator_input 
        elif operator_input == "e" or operator_input == "E": 
            operator_input = "e"
            return operator_input 
        else: 
            print("The option you chose is not a usable operator") 
            print_operators()



'''
def calculate_number(num1,num2,operator):  
    #This function calculates the input that was given through the user data
    calculation_function = operations[operator]  #This line assigns the user operator to it's function in the Dictionary
    answer = calculation_function(num1, num2) 
    if isinstance(answer, float) == True: #Just a check to see if the number is correct
        return answer 
    else: 
        print("something went wrong") 
        return "error"
''' 
