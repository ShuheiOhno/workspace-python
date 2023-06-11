import math

#素数を求めるジェネレーター
def get_primes():
    num = 2
    # 素数の時だけyield
    while True:
        if is_prime(num):
            yield num
        num += 1

#素数かどうか判定
def is_prime(val):
    result = True #素数かどうかの判定
    # 2～sqrt(val)で、valを割り切れるものがあるか
    for i in range(2, math.floor(math.sqrt(val)) + 1):
        if val % i == 0:
            result = False
            break
    return result

#素数を順に出力
for prime in get_primes():
    print(prime)
    #素数が100を超えたら終了
    if prime > 100:
        break