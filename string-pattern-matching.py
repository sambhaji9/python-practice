import re

matching = re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
print(matching)

print('tea for too'.replace('too', 'two'))
