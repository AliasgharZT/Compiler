
def is_valid_integer(s):
   
    state = 'start'
    
    for char in s:
        if state == 'start':
            if char in ['+', '-']:
                state = 'sign'
            elif char.isdigit():
                state = 'digits'
            else:
                return False
        elif state == 'sign':
            if char.isdigit():
                state = 'digits'
            else:
                return False
        elif state == 'digits':
            if not char.isdigit():
                return False
    
    return state == 'digits'  

test_inputs = ["123", "-456", "+789", "12a34", "++12", "-"]
for input_str in test_inputs:
    print(f"{input_str}: {is_valid_integer(input_str)}")

# print(f"{'++12'}: {is_valid_integer('++12')}")