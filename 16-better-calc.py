num1 = float(input('Enter first number: '))
type = input('Enter your operator: ')
num2 = float(input('Enter second number: '))

result = 'invalid operator'

if type == '/':
  result = num1 / num2
elif type == '*':
  result = num1 * num2
elif type == '-':
  result = num1 - num2
elif type == '+':
  result = num1 + num2
elif type == '//':
  result = num1 // num2
elif type == '**':
  result = num1 ** num2

print(result)