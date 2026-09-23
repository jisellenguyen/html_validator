#!/bin/python3


def validate_html(html):
    '''
    This function performs a limited version of html validation by checking whether
    every opening tag has a corresponding closing tag.

    >>> validate_html('<strong>example</strong>')
    True
    >>> validate_html('<strong>example')
    False
    '''

    # HINT:
    # use the _extract_tags function below to generate a list of html tags without
    # any extra text;
    # then process these html tags using the balanced parentheses algorithm from the
    # stack.py file.
    # The main difference between your code and the code from class will be that you
    # will have to keep track of not just the 3 types of parentheses,
    # but arbitrary text located between the html tags.

    stack = []
    for tag in _extract_tags(html):
        if not tag.startswith('</'):
            stack.append(tag)
        else:
            if len(stack) == 0:
                return False
            if _tag_name(stack[-1]) == _tag_name(tag):
                stack.pop()
            else:
                return False
    return len(stack) == 0


def _extract_tags(html):
    '''
    This is a helper function for `validate_html`.
    By convention in Python, helper functions that are not meant to be used directly
    by the user are prefixed with an underscore.

    This function returns a list of all the html tags contained in the input string,
    stripping out all text not contained within angle brackets.

    >>> _extract_tags('Python <strong>rocks</strong>!')
    ['<strong>', '</strong>']
    '''

    tags = []
    stack = []
    for i, char in enumerate(html):
        # print(f"i={i} char= {char} stack={stack} tags = {tags}")
        if char == '<':
            stack.append(char)
        elif char == '>':
            if len(stack) == 0:
                continue
            stack.append(char)
            tag = ''
            while len(stack) > 0:
                tag = stack.pop() + tag
            tags.append(tag)
        elif len(stack) > 0:
            stack.append(char)

    if len(stack) > 0:
        raise ValueError('found < without matching >')
    return tags


def _tag_name(tag):
    inner = tag.strip('<>/')
    parts = inner.split()
    if len(parts) == 0:
        return ''
    return parts[0]
