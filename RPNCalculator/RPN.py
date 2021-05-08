# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 21:33:28 2021

@author: Jan Binkowski
"""

import operator
OPERATORS = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.floordiv}
def isItANumber(num):
    try:
        float(num)
        return True
    except ValueError:
        pass
def calculator(equation):
    stack = []
    for tk in equation:
        if isItANumber(tk):
            stack.insert(0,tk)
        else:
            if len(stack) < 2:
                print('Error: Check the equation.')
                break
            else:
                print ('All values in stack: ', stack)
                operator1 = float(stack.pop(1))
                operator2 = float(stack.pop(0))
                result = OPERATORS[tk](operator1,operator2)
                stack.insert(0,str(result))                  
    return result
def main():
    while True:
        equation = input('Please enter the equation: ').split(' ')
        answer = calculator(equation)
        print('\nRESULT: ', answer)
        tryAgain = input('\nDo you want enter another equation? (type "yes" for yes)')
        if tryAgain != 'yes':
            return False
if __name__ == '__main__':
    main()
