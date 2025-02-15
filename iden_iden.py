
import keyword

def is_valid_identifier(s):
   
    state = 'start'
    
    for char in s:
        if state == 'start':
            if char.isalpha() or char == '_':
                state = 'valid'
            else:
                return False
        elif state == 'valid':
            if char.isalnum() or char == '_':
                 continue 
            else:
                return False
    
    return state == 'valid' and not keyword.iskeyword(s)  


test_identifiers = ["myVariable", "1variable", "var_1", "for", "_privateVar","_1","_x","while"]
for identifier in test_identifiers:
    print(f"{identifier}: {is_valid_identifier(identifier)}")

# print(f"{'for'}: {is_valid_identifier('for')}") 
