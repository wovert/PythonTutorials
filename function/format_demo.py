s = "{0} is {1}"
res = s.format('alex','2b')
print(res)

s1 = "{name} is {acter}"
result = s1.format(name="alex", acter="sb")
print(result)

d = {'name':'alex', 'acter':'sb'}
result2 = s1.format(**d)
print(result2)