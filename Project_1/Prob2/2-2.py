from collections import deque   
import sys
# import time

neighbor_dict = {0: (3, 1), 1: (4, 0, 2), 2: (5, 1), 3: (0, 6, 4), 4: (1, 7, 3, 5), 5: (2, 8, 4), 6: (3, 7), 7: (4, 6, 8), 8: (5, 7)}

def bfs():
    if(initial == target):
        return 0

    while frontier:
        current, depth = frontier.popleft()
        index = current.index('x')

        neighbors = {swap(current, index, j) for j in neighbor_dict[index]}      
        if target in neighbors:
            # print(f'程序占用内存: {sys.getsizeof(frontier)+sys.getsizeof(reached)}byte')
            return depth+1

        for neighbor in neighbors-reached:
            frontier.append((neighbor,depth+1))
            reached.add(neighbor)          
            
    return -1

def swap(s, i, j):
    s_list = list(s)
    s_list[i], s_list[j] = s_list[j], s_list[i]
    return ''.join(s_list)

initial = ''.join(sys.stdin.readline().split())

# 记录程序开始时间
# start_time = time.perf_counter()
    
target = "12345678x"

frontier = deque([(initial,0)])
reached = set([initial])

print(bfs())

# # 记录程序结束时间
# end_time = time.perf_counter()
# # 计算并打印运行时间
# running_time = end_time - start_time
# print(f'程序运行时间: {running_time}秒')