# evaluate the expression

def calculator(exp):
    # convert infix to postfix
    # EG: 77 / (2 * 97) -> 77 2 97 * /
    # removing brackets
    exp = exp.split()
    tmp = []
    for x in exp:
        if x[0] == '(': 
            tmp.append('(')
            tmp.append(x[1:])
        elif x[-1] == ')':
            tmp.append(x[:-1])
            tmp.append(')')
        else: tmp.append(x)
    exp = [x for x in tmp if x]
    
    stk = []
    postfix = []
    for x in exp:
        if x.isdigit():
            postfix.append(x)
        elif x in ('*', '/', '-', '+'):
            if not stk or x > stk[-1]:
                stk.append(x)
            else:
                while stk and stk[-1] >= x:
                    postfix.append(stk[-1])
                    stk.pop()
                stk.append(x)
        elif x == '(':
            stk.append('(')
        elif x == ')':
            while stk and stk[-1] != '(':
                postfix.append(stk[-1])
                stk.pop()
            stk.pop()
    for x in stk: postfix.append(x)
    
    # evaluating the postfix expression
    stk = []
    ops = '*', '/', '-', '+'
    for x in postfix:
        if x.isdigit():
            stk.append(float(x))
        elif x in ops:
            X, Y = float(stk[-2]), float(stk[-1])
            stk = stk[:-2]
            if x == '+': stk.append(X+Y)
            if x == '-': stk.append(X-Y)
            if x == '/': stk.append(X/Y)
            if x == '*': stk.append(X*Y)

    return stk[0]