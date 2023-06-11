import collections

#キュー操作(要素を末尾から追加し、先頭から取り出す)
data = collections.deque()
data.append(10)
data.append(11)
data.append(12)
print(data) # deque([10, 11, 12])
print(data.popleft()) # 10
print(data) # deque([11, 12])

#スタック操作(要素を末尾から追加し、末尾から取り出す)
data2 = collections.deque()
data2.append(10)
data2.append(11)
data2.append(12)
print(data2) # deque([10, 11, 12])
print(data2.pop()) # 12
print(data2) # deque([10, 11])
