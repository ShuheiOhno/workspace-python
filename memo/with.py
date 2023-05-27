#ファイルを開き終わったら自動でクローズ
# 上書き
with open('test.txt','w') as f:
    f.write('AAA')
#読み込み
with open('test.txt', 'r') as f:
    print(f.read())
