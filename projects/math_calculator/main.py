import sys
from datetime import datetime
import logging
from utils import validator
from utils import calculator

logging.basicConfig(filename='logs/app.log', level=logging.DEBUG)

try:
    today = datetime.now()
    print('Mathematical Expression Validator &')
    print('Enter your expression or \'exit\' to quit > ', end='')
    exp = input()
    is_valid = validator.is_valid_expression(exp)
    if is_valid:
        ans = calculator.calculator(exp)
        logging.info(f'{today:%Y-%m-%d %H:%M:%S} - INFO - Valid expression: {exp}')
        print(f'The result is: {ans}')
        logging.info(f'{today:%Y-%m-%d %H:%M:%S} - INFO - Result of the expression is: {ans}')
        logging.info(f'{today:%Y-%m-%d %H:%M:%S} - INFO - Exiting program')
    elif not is_valid:
        logging.error(f'{today:%Y-%m-%d %H:%M:%S} - ERROR - Invalid expression!')
        logging.info(f'{today:%Y-%m-%d %H:%M:%S} - INFO - Exiting program')
        print('Invalid expression')
    elif expr == 'exit':
        print('bye bye!')
        logging.info(f'{today:%Y-%m-%d %H:%M:%S} - INFO - Exiting program')
        sys.exit(0)
    else:
        print('The expression is not valid.')
except:
    print('Error calculating the expression')