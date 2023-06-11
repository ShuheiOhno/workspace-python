def my_func(value, list=[]):
    list.append(value)
    return list

print(my_func(10)) # [100]
print(my_func(11)) # [10, 11] リストはミュータブルだから
print(my_func(12, [33, 34])) # [33, 34, 12]
print(my_func(12, [33, 34])) # [33, 34, 12]

#修正版
def my_func2(value, list=None):
    if list is None:
        list = []
    list.append(value)
    return list

print(my_func2(10)) # [100]
print(my_func2(11)) # [11]
print(my_func2(12, [33, 34])) # [33, 34, 12]
print(my_func2(12, [33, 34])) # [33, 34, 12]