import itertools
data1 = ['パンダ', 'ウサギ', 'コアラ', 'トラ']
data2 = ['panda', 'rabbit', 'koala']

for d1, d2 in itertools.zip_longest(data1, data2):
    print(d1, " = ", d2)