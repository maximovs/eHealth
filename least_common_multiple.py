# A naive solution would be to get the maximum value of the array and add itself until the value is the lcm. But it is not performant, mainly when the array is big.
# An other solution would be to get the prime factorization of the values in the array and get the max exponent of each prime. It is well known that there is no performant way to do this.
# So the solution I've implemented is calculating the LCM by first using the euclidean algorithm (which is very performant!) to calculate the GCD and then use it to calculate the LCM.

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a


def euclidean_lcm(a, b):
    return a * b / gcd(a,b)

array = [26098, 67, 31, 27, 23, 19, 17, 13, 11]
print reduce(euclidean_lcm, array)