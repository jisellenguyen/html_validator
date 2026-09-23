def balanced_parens(text):
    '''
    Checks whether every opening parenthesis has a corresponding closing parenthesis of a matching type.

    >>> balanced_parens('(()())')
    True
    >>> balanced_parens('(()(()((()))))()(())')
    True
    >>> balanced_parens('([]{})')
    True
    >>> balanced_parens('([]{[][]{{()}}})')
    True
    >>> balanced_parens('([}[})')
    False
    >>> balanced_parens(')))(((')
    False
    >>> balanced_parens('(()()')
    False
    >>> balanced_parens('(()()))')
    False

    Not all characters need to be parentheses.

    >>> balanced_parens('(hello)(world)')
    True
    >>> balanced_parens('(salve{hola[mundo]}munde)')
    True
    >>> balanced_parens('(salve[)munde]')
    False
    '''
    stack = []
    for i, char in enumerate(text):
        #  print(f"i={i} char= {char} stack={stack}")
        if char in '([{':
            # append = push
            stack.append(char)
        elif char in ')]}':
            if len(stack) == 0:
                return False
            # stack[-1] = top
            # last thing pushed
            if (stack[-1] == '(' and char == ')') or \
               (stack[-1] == '[' and char == ']') or \
               (stack[-1] == '{' and char == '}'):
                stack.pop()
            else:
                return False
    return len(stack) == 0
