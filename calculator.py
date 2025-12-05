#calculator.py (this is the main file)

import calculator_functions 
from continuous_calculator import ContinuousCalculator

my_calc = ContinuousCalculator(initial_value=0.0) 

while(True): 
    my_calc.print_result()
    calculator_functions.print_operators() 
    operator = calculator_functions.get_operator()  
    if operator == "c": 
        my_calc.clear() 
        continue 
    if operator == "n": 
        print("Type in your new float value")
        new_float = calculator_functions.get_float_input()
        my_calc.set_value(new_float)
        continue
    if operator == "e": 
        exit()
    print("Type in a floating point number to "+ calculator_functions.operations_strings[operator]) 
    float_modifier = calculator_functions.get_float_input() 
    my_calc.calculate(operator,float_modifier)
