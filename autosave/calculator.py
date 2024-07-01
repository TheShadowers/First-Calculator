

def is_valid(expression):
    valid_chars = "0123456789+-*/() "
    for char in expression:
        if char not in valid_chars:
            return False
    return True
    
    
while True:
    calc_op = input("What do you want to calculate?\n")
    if is_valid(calc_op):  
        if "+" in calc_op:
            operands = calc_op.split("+")
            print(float(operands[0])+float(operands[1]))
        elif "-" in calc_op:
            operands = calc_op.split("-")
            print(float(operands[0])-float(operands[1]))
        elif "/" in calc_op:
            operands = calc_op.split("/")
            print(float(operands[0]) / float(operands[1]))
        elif "*" in calc_op:
            operands = calc_op.split("*")
            print(float(operands[0])*float(operands[1]))          
    else:
        print("Invalid input, try again.")
    
    
    
 