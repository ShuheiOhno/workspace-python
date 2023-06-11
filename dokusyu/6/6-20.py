title = ['部長', '課長', '係長', '主任']
data = [
    {'name':'高橋', 'position' : '主任'},
    {'name':'鈴木', 'position' : '係長'},
    {'name':'佐藤', 'position' : '部長'},
    {'name':'加藤', 'position' : '課長'},
]

data.sort(key=lambda x: title.index(x['position']))
print(data)