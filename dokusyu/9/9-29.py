import asyncio
import time

async def heavy_process(name, sec):
    print(f'start {name}')

    await asyncio.sleep(sec)
    print(f'end {name}')
    return f'{name}/{sec}'


loop = asyncio.get_event_loop()
result = loop.run_until_complete(
    asyncio.gather(
        heavy_process('aaa', 2),
        heavy_process('bbb', 5),
        heavy_process('ccc', 1),
        heavy_process('ddd', 3),
    )
)
"""
start aaa
start bbb
start ccc
start ddd
end ccc
end aaa
end ddd
end bbb
"""