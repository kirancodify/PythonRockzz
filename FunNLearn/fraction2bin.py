fraction = float(raw_input('Enter a decimal number between 0 and 1: '))

p = 0
while ((2**p)*fraction)%1 != 0:
    print('Remainder = ' + str((2**p)*fraction - int((2**p)*fraction)))
    p += 1

num = int(fraction*(2**p))

result = ''
if num == 0:
    result = '0'
while num > 0:
    result = str(num%2) + result
    num = num/2

for i in range(p - len(result)):
    result = '0' + result

result = result[0:-p] + '.' + result[-p:]
print('The binary representation of the decimal ' + str(fraction) + ' is ' + str(result))