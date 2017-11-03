import re

def get_num(i):
    s = str(i)
    result = ''
    if re.match('.*3.*', s) != None: result = 'Fizz'
    if re.match('.*5.*', s) != None: result += 'Buzz'

    return s if len(result) == 0 else result

def fizzbuzz():
    return [get_num(i) for i in range(1, 100)]

print(fizzbuzz())
