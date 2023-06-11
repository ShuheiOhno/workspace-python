# for i in range(1, 10):
#     data = [i * j for j in range(1, 10)] 


#解答
for i in range(1, 10):
    for j in range(1, 10):
        result = i * j
        print(f"{result} ", end='')
    print()