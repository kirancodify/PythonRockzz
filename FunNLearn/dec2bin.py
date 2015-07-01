# Take a input
decimal = int(raw_input("Enter a decimal number:"))
# Check for negative
if decimal < 0:
    isNeg = True
    decimal = abs(decimal)
else:
    isNeg = False
result = ''
# Convert to binary
if decimal == 0:
    result = '0'

while decimal > 0:
    result = str(decimal%2) + result
    decimal = decimal/2
if isNeg:
    result = '-' + result
print result