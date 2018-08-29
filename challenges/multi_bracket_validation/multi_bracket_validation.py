# from stack.stack import Stack
from ... data_structures.stack.stack import Stack


def multi_bracket_validation(input):
    """ Input is a string. Output is a Boolean
        Testing if the brackets of string are balanced
    """
    s = Stack()
    pairs = {')': '(', ']': '[', '}': '{'}
    for char in input:
        if char in pairs.values():
            s.push(char)
        elif char in pairs.keys():
            if pairs[char] == s.peek():
                s.pop()
            else:
                return False
    if len(s):
        return False
    return True


if __name__ == '__main__':
    winner = multi_bracket_validation(str(input('Input here >: ')))
    if winner:
        print('You Did It!')
    else:
        print('Do Better')
