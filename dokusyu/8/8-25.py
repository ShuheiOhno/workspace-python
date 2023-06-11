def create_dict(**kwargs):
    result = dict()
    for key, val in kwargs.items():
        result[key] = val
    return result
d = create_dict(name='佐藤', age=30, sex='male')
print(d) # {'name': '佐藤', 'age': 30, 'sex': 'male'}