data = [
    '犬',
    '猫',
    'ゴリラ',
    'シャチ',
    'いるか',
    '鳥',
    'タコ',
]

result = filter(lambda x : len(x) < 3, data)
print(list(result)) #['犬', '猫', '鳥', 'タコ']
# result = [x for x in data if len(x) < 8] と同じ