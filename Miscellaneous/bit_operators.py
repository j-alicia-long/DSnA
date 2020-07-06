### Bitwise operators

a = 10
b = 4

# Print bitwise AND operation
print("a & b =", a & b)     # 0

# Print bitwise OR operation
print("a | b =", a | b)     # 14

# Print bitwise NOT operation
print("~a =", ~a)           # -11

# print bitwise XOR operation
print("a ^ b =", a ^ b)     # 14


### Shift operators

a = 10
b = -10

# print bitwise right shift operator
print("a >> 1 =", a >> 1)       # 5
print("b >> 1 =", b >> 1)       # -5 ??
# need to study neg conversion and two's complement again

a = 5
b = -10

# print bitwise left shift operator
print("a << 1 =", a << 1)       # 10
print("b << 1 =", b << 1)       # -20


### Bit count
print(bin(a ^ b).count('1'))
