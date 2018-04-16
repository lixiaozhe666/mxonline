# import re
#
# pattern = re.compile(r'\d+')
# print re.split(pattern, 'one12222two2three3four4')

import re
pattern = re.compile(r'(one)(one)')
result =  re.match(pattern, 'oneone2three3four4')
print result.group()
print result.groups()