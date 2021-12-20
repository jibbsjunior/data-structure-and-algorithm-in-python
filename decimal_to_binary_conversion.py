# In this coding exercise, you are required to use the stack data structure to convert integer values to their binary equivalent.
# I will use the division by 2 method in this challenge to convert a decimal number to binary
# print(60 % 2)
from stack import Stack
def dec_to_bin(stack, dec_num):
    if dec_num == 0:
        return 0
    temp = []
    bin_num = ""
    temp.append(dec_num)
    while dec_num > 1:
        temp.append(dec_num//2)
        dec_num = dec_num//2
    for i in temp:
        stack.push(i%2)
    while not stack.is_empty():
        bin_num += str(stack.pop())
    return bin_num

# Another method that optimize the function to use 1 argument
def decimal_to_binary(dec_num):
    if dec_num == 0:
        return 0

    s = Stack()

    while dec_num > 0:
        remainder = dec_num % 2
        s.push(remainder)
        dec_num = dec_num // 2

    bin_num = ""
    while not s.is_empty():
        bin_num += str(s.pop())

    return bin_num

# s = Stack()
# # dec = 112
# print(dec_to_bin(s, 12))
# print(dec_to_bin(s, 112))
# print(dec_to_bin(s, 60))
# print(dec_to_bin(s, 27))
# print(dec_to_bin(s, 48))
# print(dec_to_bin(s, 98))
print(decimal_to_binary(21))

