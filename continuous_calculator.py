#continuous_calculator

import calculator_functions

#A calculator that keeps track of a running total.
class ContinuousCalculator:
    
    def __init__(self, initial_value=0.0):
        #Holds the current result
        self.result = initial_value
        
        # Mapping symbols to the imported functions
        self.operations = {
            "+": calculator_functions.add,
            "-": calculator_functions.subtract,
            "*": calculator_functions.multiply,
            "/": calculator_functions.divide
        }

    #Uses imported functions to calculate and change the current result
    def calculate(self, operation_symbol, next_number):
        # Check if the operation is correct
        if operation_symbol not in self.operations:
            return "Error: Invalid operation."
        
        calculation_function = self.operations[operation_symbol]
        
        # Calculate the new result
        new_result = calculation_function(self.result, next_number)
        
        # Update the result)
        self.result = new_result
        
        return self.result

    #get current result
    def get_result(self):
        return self.result 
    
    #print current result
    def print_result(self): 
        print("Your current number is " + str(self.result))
        
    #sets result to 0
    def clear(self):
        self.result = 0.0
        return "Calculator cleared."
    
    #sets the result to the imported value
    def set_value(self, new_value):
        self.result = new_value 
        return new_value 
