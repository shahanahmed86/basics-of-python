employees = open('./employees.txt', 'r')

for employee in employees.readlines():
  print(employee)

employees.close()