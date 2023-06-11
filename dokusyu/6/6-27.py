data1 = [1, 3, 5]
data2 = [2, 7, 10]

result = map(lambda x1, x2: x1 * x2, data1, data2)
print(list(result)) #[2, 21, 50]