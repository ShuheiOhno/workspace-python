# リストはミュータブル
data1 = [1, 2, 3]
data2 = data1
data1[0] = 100
print(data1)
print(data2)


#intはイミュータブル
x = 1
y = x
x += 10
print(x)
print(y)