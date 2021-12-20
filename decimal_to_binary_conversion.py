# In this coding exercise, you are required to use the stack data structure to convert integer values to their binary equivalent.
# I will use the division by 2 method in this challenge to convert a decimal number to binary
# print(60 % 2)
from stack import Stack
def dec_to_bin(stack, dec_num):
    value = []
    bin_num = []
    # stack.push(dec_num // 2)
    # temp = dec_num//2
    while dec_num > 0.1:
        value.append(dec_num//2)
        # stack.push(value[i]%2)
        # dec_to_bin//2
        dec_num = dec_num//2
        # while not stack.is_empty():
        #     bin_num += stack.pop()                                                        
    # return value
    for i in value:
        stack.push(i%2)
    while not stack.is_empty():
        bin_num.append(stack.pop())
    return bin_num


s = Stack()
dec = 31
print(dec_to_bin(s, dec))
# print(dec_to_bin(60))


