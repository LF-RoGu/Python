# Owner: Luis Fernando Rodriguez Gutierrez
#IDE: PyCharm
#Institution: FH-Dortmund
#Matriculation Number: 

def funct_factorial(varFactorial):
    tempValue = 0
    if(varFactorial < 0):
        return "Cannot calculate negative numbers"
    elif(varFactorial == 0) or (varFactorial == 1):
        tempValue = 1
        return tempValue
    else:
        tempValue = 1
        for index in range(2, varFactorial+1):
            tempValue *= index
        return tempValue

if __name__ == '__main__':
    factNumber = 10
    # f-string format to print a text and numbers at the same time
    print(f"Factorial of {factNumber}... {funct_factorial(factNumber)}")
