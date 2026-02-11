'''
    A non-negative numbers can be expressed as e.g. [2, 0, 1] = 2 * 3^0 + 0 * 3^1 + 1* 3^2 = 11
    return the number represented by l + 1 in 0, 1, 2 format
'''

# 直接模拟“三进制加一”
def successor(l):
    carry = 1
    for i in range(len(l)):
        l[i] += carry
        if l[i] == 3:
            l[i] = 0
            carry = 1
        else:
            carry = 0
    if carry:
        l.append(carry)
    return l

print(successor([2,0,1]))