from operator import itemgetter
sample = [[1000, 'Bob'], [100, 'Mary'], [10, 'Alex']]

sample.sort(key=lambda x: x[1])
print(sample)

x = lambda x: x ** 5

print(x(6))
