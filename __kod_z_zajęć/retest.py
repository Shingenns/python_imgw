import re

digits = re.compile('[0-9]')


print(re.findall(digits, '7s76dfy7syd7yyf7d'))
print(re.finditer(digits, '7s76dfy7syd7yyf7d'))
print(re.match(digits, '7s76dfy7syd7yyf7d'))
print(re.fullmatch(digits, '7s76dfy7syd7yyf7d'))

fval = re.compile(r'[0-9\s]+[.,][0-9]+')

print(re.findall(fval, '1 435.34343'))
print(re.findall(fval, 'etrt 1 435.34343 tert'))
print(re.findall(fval, '1 435,34343'))
print(re.findall(fval, '1435.0'))