import asyncio
import time

# 疑似的な重い処理
async def heavy_process(name, sec):
    print(f'start {name}')

    # ダミーの重い処理
    await asyncio.sleep(sec)
    print(f'end {name}')
    return f'{name}/{sec}'

# print(heavy_process('Hoge', 5))
start = time.time()
loop = asyncio.get_event_loop()
result = loop.run_until_complete(
    heavy_process('Hoge', 5)
)
end = time.time()
print(result)
print(f'Process Time: {end - start}')
"""
start Hoge
end Hoge
Hoge/5
Process Time: 5.014143705368042
"""