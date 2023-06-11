#デコレーターを使わない場合
def log_func(func):
    def inner(*args, **keywds):
        print('-----------------')
        print(f'Name: {func.__name__}')
        print(f'Args: {args}')
        print(f'keywds: {keywds}')
        print('-----------------')
        return func(*args, **keywds)
    return inner

def hoge(x, y, m='bar', n='piyo'):
    print(f'hoge: {x} - {y}/ {m} - {n}')

# log_func関数の戻り値を実行
log_hoge = log_func(hoge)
log_hoge(15, 37, m='ほげ', n='ぴよ')