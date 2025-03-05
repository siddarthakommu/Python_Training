import re

def is_valid_expression(exp):
    return bool(re.match('[0-9/*-+ ()]', exp))