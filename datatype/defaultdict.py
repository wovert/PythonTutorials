from collections import defaultdict

values = [11,22,33,44,55,66,77,88,99,90]
dic = defaultdict(list)
for value in values:
  if value > 66:
    dic['k1'].append(value)
  else:
    dic['ke2'].append(value)

print(dic)