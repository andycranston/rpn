#! /usr/bin/python3
#
# @(!--#) @(#) rpncalc.py, version 001, 05-september-2018
#
# simple reverse polish notation calculator
#

################################################################################################

#
# imports
#

import sys
import os
import argparse
import time
import datetime

################################################################################################

################################################################################################

def topofstack(s):
    if len(s) == 0:
        print('<stack empty>')
    else:
        print(s[-1])

    return

################################################################################################
def main():
    funcname = 'main'    

    stack = []

    while True:
        try:
            line = input('RPN>').strip()
        except KeyboardInterrupt:
            print('')
            break
        
        if line.lower() == 'exit':
            break
        
        if len(line) == 0:
            continue
        
        if line == '.':
            topofstack(stack)
            continue
        
        if line == '..':
            stacksize = len(stack)
            
            if stacksize == 0:
                print('<stack empty>')
            else:
                i = stacksize - 1
                while (i >= 0) and (i >= (stacksize - 10)):
                    print(stack[i])
                    i -= 1
                if stacksize > 10:
                    print('<more than 10 items on stack>')
            continue                
                
        if line.lower() == 'drop':
            if len(stack) == 0:
                print('<stack already empty>')
            elif len(stack) == 1:
                stack = []
            else:
                stack = stack[0:-1]
            continue
        
        if line.lower() == 'dropall':
            stack = []
            continue
        
        if line == '+':
            if len(stack) < 2:
                print('<too few items on stack>')
            else:
                sum = stack[-2] + stack[-1]
                stack[-2] = sum
                del stack[-1]
                topofstack(stack)
            continue
        
        if line == '-':
            if len(stack) < 2:
                print('<too few items on stack>')
            else:
                subtract = stack[-2] - stack[-1]
                stack[-2] = subtract
                del stack[-1]
                topofstack(stack)
            continue
        
        if line == '*':
            if len(stack) < 2:
                print('<too few items on stack>')
            else:
                product = stack[-2] * stack[-1]
                stack[-2] = product
                del stack[-1]
                topofstack(stack)
            continue
        
        if line == '/':
            if len(stack) < 2:
                print('<too few items on stack>')
            else:
                if stack[-1] == 0:
                    print('<no possible - division by zero would result>')
                else:
                    division = stack[-2] / stack[-1]
                    stack[-2] = division
                    del stack[-1]
                    topofstack(stack)
            continue
        
        try:
            fpnum = float(line)
        except ValueError:
            print('<invalid number>')
            continue
            
        stack.append(fpnum)

    return
        
##########################################################################

progname = os.path.basename(sys.argv[0])

sys.exit(main())

# end of file
