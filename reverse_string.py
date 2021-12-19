#Method - 1 to reverse a string
# input_str = "Ajibola"
# print(input_str[::-1])

#Method - 2 to reverse a string (using stack)
from stack import Stack
def reverse_string(stack, input_str):
    for i in range(len(input_str)):
        stack.push(input_str[i])
        # print(stack)  
    reverse_str = ""
    while not stack.is_empty():
        reverse_str += stack.pop()
        # print(reverse_str)
    return reverse_str

s = Stack()
input_str = "!airegiN ot emocleW"
print(reverse_string(s, input_str))