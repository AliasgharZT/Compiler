
def is_valid_decimal(s):

    state = 'start'
    
    for char in s:
        if state == 'start':
            if char in ['+', '-']:
                state = 'sign'
            elif char.isdigit():
                state = 'integer'
            else:
                return False
        elif state == 'sign':
            if char.isdigit():
                state = 'integer'
            elif char == '.':
                state = 'decimal_point'
            else:
                return False
        elif state == 'integer':
            if char.isdigit():
                continue  
            elif char == '.':
                state = 'decimal_point'
            else:
                return False
        elif state == 'decimal_point':
            if char.isdigit():
                state = 'fraction'
            else:
                return False
        elif state == 'fraction':
            if not char.isdigit():
                return False
    
    return state in ['integer', 'fraction']  

# test_inputs = ["123.45", "-456.78", "+789", "12.34a", "++12", "-."]
# for input_str in test_inputs:
#     print(f"{input_str}: {is_valid_decimal(input_str)}")
print(f"{'12.34a'}: {is_valid_decimal('12.34a')}") 