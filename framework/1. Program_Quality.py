import string
import pandas as pd

def check_qul(statement):
    statement=str(statement)
    bad_quality=["=",".",",","(","_"]
    py_operators = ['+', '-', '*', '/', '//', '%', '>', '<', '=']
    last_char=statement[-1]
    quality=False
    if last_char in bad_quality or last_char in py_operators:
        quality=False
    else:
        quality=True
    return quality

def balanced(statement):
    s=str(s)
    pairs = {"{": "}", "(": ")", "[": "]"}
    stack = []
    for c in s:
        if c in "{[(":
            stack.append(c)
        elif stack and c == pairs[stack[-1]]:
            stack.pop()
        else:
            return False
    return len(stack) == 0
