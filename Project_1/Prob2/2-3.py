import heapq
import sys
# import time

neighbor_dict = {0: (3, 1), 1: (4, 0, 2), 2: (5, 1), 3: (0, 6, 4), 4: (1, 7, 3, 5), 5: (2, 8, 4), 6: (3, 7), 7: (4, 6, 8), 8: (5, 7)}

def dijkstra():
    while frontier:
        depth, current = heapq.heappop(frontier)
        if(current == target):
            return depth       
        index = current.index('x')

        neighbors = {swap(current, index, j) for j in neighbor_dict[index]}       
        for neighbor in neighbors-reached:
            heapq.heappush(frontier, (depth+1, neighbor))
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

frontier = []
heapq.heappush(frontier,(0,initial))
reached = set([initial])

print(dijkstra())

# # 记录程序结束时间
# end_time = time.perf_counter()
# # 计算并打印运行时间
# running_time = end_time - start_time
# print(f'程序运行时间: {running_time}秒')