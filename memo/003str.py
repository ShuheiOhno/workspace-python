# ローデータにする場合　rを先頭につける
print(r'C:\user\test')

# エラー
# print('C:\user\test')


# \で空白を消す
print("""\
複数行

複数行\
""")

# インデックス
word ='abcdeb is string'
print(word[1])
print(word[0])
print(word[-1])
print(word[1:3])
print(word[1:])

#文字数
print('文字数:' + str(len(word)))

# aで始まっているかどうか
is_start = word.startswith('a')
print(is_start)

# bがどこにあるか調べる（初め（0）から数えて何番目か)
print(word.find('b'))
#後ろのbは、rfind(初め（0）から数えて何番目か)
print(word.rfind('b'))

# bがいくつあるかカウント
print(word.count('b'))

# 最初の文字だけ大文字に変換
print(word.capitalize())
# 単語の最初の文字を大文字に変換
print(word.title())
# すべて大文字に変換
print(word.upper())
# すべて大文字に変換
print(word.lower())

# リプレイス
print(word.replace('b', '777'))

# △format
str = '{1} {0} {2}'.format(1,2,3)
print(str)

# fstring
x,y,z = 1,2,3
print(f'f-string is {x} {y} {z}')