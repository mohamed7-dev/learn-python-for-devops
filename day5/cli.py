import sys
import calc

def runCLI():
    operand1 = float(sys.argv[1])
    operator = sys.argv[2]
    operand2 = float(sys.argv[3])

    if(operator == "plus"):
        calc.add(operand1,operand2)
    elif (operator == "times"):
        calc.multiply(operand1,operand2)
    else:
        print("Invalid operation!")     
        
runCLI()