import sys
# import time

# 记录程序开始时间
#start_time = time.perf_counter()

n,m = map(int, sys.stdin.readline().split())

graph = [[10000000 for _ in range(n+1)] for _ in range(n+1)]    #a-b的最短距离
for i in range(0,m):
    a,b,c = map(int, sys.stdin.readline().split())
    graph[a][b] = min(graph[a][b],c)

reached = {}         

dis_to_root = [10000000 for _ in range(n+1)]    
dis_to_root[1] = 0

for i in range(0,n):
    current = -1
    for j in range(1,n+1):
        if((j not in reached) and (current == -1 or dis_to_root[current]>dis_to_root[j])):
            current = j
            
    reached[current] = current
    for k in range(1,n+1):
        dis_to_root[k] = min(dis_to_root[k],dis_to_root[current]+graph[current][k])

if(dis_to_root[n] == 10000000):
    print(-1)
else:
    print(dis_to_root[n])

# 记录程序结束时间
#end_time = time.perf_counter()

# 计算并打印运行时间
# running_time = end_time - start_time
# print(f'程序运行时间: {running_time}秒')
# print(f'程序占用内存: {sys.getsizeof(graph)+sys.getsizeof(reached)+sys.getsizeof(dis_to_root)}byte')