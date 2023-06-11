#高階関数
def walk_list(data, func):
    for key, val in enumerate(data):
        func(val, key)

def show_item(value, key):
    print(key, ':', value)

data = [1, 2, 12, 32, 5]
walk_list(data, show_item)
"""
0 : 1
1 : 2
2 : 12
3 : 32
4 : 5
"""