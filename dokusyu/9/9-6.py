def my_gen():
    yield 'あいうえお'
    yield 'aaaaa'
    yield 'nnnnn'

for val in my_gen():
    print(val)
"""
あいうえお
aaaaa
nnnnn
"""