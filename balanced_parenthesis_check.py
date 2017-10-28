# Interview question for `Stack`.
# Given a string of opening and closing parenthesis, check whether it's balanced or not.
# examples:
#   '[()]' is balanced
#   '[(])' is not balanced

def balanced_check(s):

    if len(s) % 2 != 0:
        return False

    opening = set('([{')
    matches = set([  ('(',')'),  ('[',']') , ('{','}') ])

    stack = []

    for parenthesis in s:

        if parenthesis in opening:
            stack.append(parenthesis)

        else:
            if len(stack) == 0:
                return False

            last_opening = stack.pop()

            if (last_opening, parenthesis) not in matches:
                return False

    return len(stack) == 0