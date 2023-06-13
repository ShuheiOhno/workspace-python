import asyncio
import time

async def heavy_process(name, sec):
    print(f'start {name}')

    await asyncio.sleep(sec)
    print(f'end {name}')
    return f'{name}/{sec}'

#非同期処理のエントリーポイント
async def main():
    #コルーチンをそのままawait式に渡した場合
    # print(await heavy_process('aaa', 2))
    # print(await heavy_process('bbb', 5))
    # print(await heavy_process('ccc', 1))
    
    #Taskに書き換え
    t1 = asyncio.create_task(heavy_process('aaa', 2))
    t2 = asyncio.create_task(heavy_process('bbb', 5))
    t3 = asyncio.create_task(heavy_process('ccc', 1))
    print(await t1)
    print(await t2)
    print(await t3)

start = time.time()
loop = asyncio.get_event_loop()
asyncio.run(main())
end = time.time()
print(f'Process Time: {end - start}')
"""
start aaa
start bbb
start ccc
end ccc
end aaa
aaa/2
end bbb
bbb/5
ccc/1
Process Time: 5.019620895385742
"""