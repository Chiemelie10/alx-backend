dic = ['one', 'two', 'three', 'four']

value = iter(dic)

for _ in range(2):
    next_item = next(value)
    print(next_item)
