import ast

with open('brackets.txt', 'r') as file:
    data = file.read()
data = data.replace('\n', '').replace(' ', '')

try:
    bracket_list = ast.literal_eval(data)
except Exception as e:
    print("Error parsing the bracket data:", e)
    exit()
    
flag_chars = []
for idx, sublist in enumerate(bracket_list):
    if isinstance(sublist, list):
        element_count = len(sublist)
        print(f"Sublist {idx+1} has {element_count} elements")
        if 32 <= element_count <= 126:
            flag_chars.append(chr(element_count))
        else:
            print(f"Element count {element_count} is out of printable ASCII range.")
    else:
        print(f"Sublist {idx+1} is not a list.")
flag = ''.join(flag_chars)
print("\nExtracted Flag:", flag)
