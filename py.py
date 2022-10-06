def simple():
    for i in range(20):
        yield i
x = simple()
for j in x:
    print(j)
