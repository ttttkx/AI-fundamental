import queue
import sys
# import time

# 记录程序开始时间
#start_time = time.perf_counter()

n,m = map(int, sys.stdin.readline().split())

graph = {i: [] for i in range(1, n+1)}     
for i in range(0,m):
    a,b = map(int, sys.stdin.readline().split())
    graph[a].append(b)

frontier = queue.Queue()    
frontier.put(1)

reached = {}        
reached[1] = 1

dis_to_root = [0 for _ in range(n+1)]    

isFind = 0

# 从队列中获取元素
while not frontier.empty():
    node = frontier.get()
    for child in graph[node]:
        if(child not in reached):
            dis_to_root[child] = dis_to_root[node]+1
        if(child == n):
            print(dis_to_root[child])
            isFind = 1
            break
        if(child not in reached):
            reached[child] = child
            frontier.put(child)
    if(isFind == 1):
        break

if(isFind == 0):
    print(-1)

# 记录程序结束时间
#end_time = time.perf_counter()

# 计算并打印运行时间
# running_time = end_time - start_time
# print(f'程序运行时间: {running_time}秒')
# print(f'程序占用内存: {sys.getsizeof(graph)+sys.getsizeof(reached)}byte')