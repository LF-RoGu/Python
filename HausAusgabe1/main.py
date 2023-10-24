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

def funct_chessBoard(varRows, varCols):
    varChess = ""
    for index_i in range(varRows):
        varChess = ""
        for index_j in range(varCols):
            if((index_i + index_j) % 2 == 0):
                # The space is for aestetics, as it looked weird
                varChess += '* '
            else:
                varChess += '  '
        print(varChess)
    print()
if __name__ == '__main__':
    factNumber = 10
    # f-string format to print a text and numbers at the same time
    print(f"Factorial of {factNumber}... {funct_factorial(factNumber)}")

    funct_chessBoard(8,8)
