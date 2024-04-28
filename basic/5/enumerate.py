list = ['aaa', 'bbb', 'ccc']
for i, val in enumerate(list):
    print(f'{i}: {val}')


print('--------------zip------------')
days = ['Mon', 'Tue', 'Wed']
fruits = ['apple', 'banana', 'orange']
drinks = ['coffee', 'tea', 'beer']

for day, fruit, drink in zip(days, fruits, drinks):
    print(f'{day} {fruit} {drink}')

print('---------------dict--------------')
def menu(**kwargs):
    for k, v in kwargs.items():
        print(k , v)
d = {
    'entree': 'beef',
    'drink': 'coffee',
    'dessert': 'ice'
}

menu(**d)
# menu({'a':10, 'b': 20})  error
# menu({'a': '10', 'b': '20'})  error
menu(a=10, b=20)


print('---------------closer--------------')
def outer(a, b):

    def inner():
        return a + b
    
    return inner

print(outer(1,2)) #　まだ実行されない
f = outer(1,2)
r = f() #　ここで実行
print(r)

def circle_area_func(pi):
    def circle_area(radius):
        return pi * radius * radius
    
    return circle_area

ca1=circle_area_func(3.14)
ca2=circle_area_func(3.141592)

print(ca1(10))
print(ca2(10))

print('---------------decorator--------------')
def print_info(func):
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return wrapper

@print_info
def add_num(a,b):
    return a + b

# f = print_info(add_num)
# r = f(10, 20)
# print(r)

@print_info
def sub_num(a, b):
    return a - b

r = add_num(10,20)
print(r)
r = sub_num(10,20)
print(r)
print('------')
def print_more(func):
    def wrapper(*args, **kwargs):
        print('func:', func.__name__)
        print('args:', args)
        print('kwargs:', kwargs)
        result = func(*args, **kwargs)
        print('result:', result)
        return result
    return wrapper

@print_more
def add_num_more(a, b):
    return a + b

r = add_num_more(11,12)
# r = add_num_more(11,12,13) # error
print(r)

print('-----------------------lambda---------------------')
# lambda書き換え前
l = ['Mon', 'tue', 'Wed', 'Thu', 'fri', 'sat', 'Sun']

def change_words(words, func):
    for word in words:
        print(func(word))

def sample_func(word):
    return word.capitalize()

change_words(l, sample_func)

# lambdaで書き換え functionを引数とするもの
# sample_func = lambda word: word.capitalize()
change_words(l, lambda word: word.capitalize())
change_words(l, lambda word: word.lower())


print('-----------------------generator---------------------')
def greeting():
    yield 'Good morning'
    yield 'Good afternoon'
    yield 'Good night'

g = greeting()
print(next(g))
print(next(g))
print(next(g))
# print(next(g))

def counter(num=10):
    for _ in range(num):
        yield 'run'

c=counter()
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))

# print(next(g))

print(next(c))
print(next(c))


print('-----------------------リスト内包---------------------')
t = (1,2,3,4,5)
t2 = (5,6,7,8,9)
r =[]
for i in t:
    r.append(i)
print(r)

r = [i for i in t]
print(r)

r = []
for i in t:
    for j in t2:
        r.append(i * j)
print(r)

r = [i * j for i in t for j in t2]
print(r)

print('-----------------------辞書内包---------------------')
w = ['mon', 'tue', 'wed']
f = ['coffee', 'milk', 'water']

d = {}
for x, y in zip(w, f):
    d[x] = y
print(d)

d = {x: y for x, y in zip(w, f)}
print(d)


print('-----------------------集合内包---------------------')
s = set()
for i in range(10):
    s.add(i)
print(s)

s = {i for i in range(10)}
print(s)



print('-----------------------ジェネレータ内包---------------------')
def g():
    for i in range(10):
        yield i
g = g()
g = (i for i in range(10) if i % 2 == 0)
print(g)
print(type(g))
for x in g:
    print(x)


print('-----------------------辞書内包---------------------')
print('-----------------------辞書内包---------------------')
print('-----------------------辞書内包---------------------')