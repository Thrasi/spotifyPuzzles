import sys
for line in sys.stdin.readlines():
    inputN = int(line)
n = inputN
nMax = 1e9
binary = []
while n%2 or n/2:
    binary.append(n%2)
    n=n/2
binary = binary[::-1]
#print "Decimal: {0}, Binary: {1}".format(inputN,binary)
reverseDecimal = 0
for power in range(len(binary)):
    reverseDecimal = reverseDecimal +  binary[power]*(2**power)

reverseBinary = binary[::-1]
#print "Decimal: {0}, Binary: {1}".format(reverseDecimal,reverseBinary)
print reverseDecimal
    