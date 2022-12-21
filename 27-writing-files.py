# this will create a new file
html_file = open('./index.html', 'w')
html_file.write('<h1>Hello world</h1>')
html_file.close()

# this will append the content to the file
employees_file = open('./employees.txt', 'a')
employees_file.write('\nToby - Human Resources')
employees_file.close()
