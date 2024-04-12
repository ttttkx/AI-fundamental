import heapq
import sys
# import time

def inversions(state):
    count = 0
    state.remove(0)
    for i in range(8):
        for j in range(i + 1, 8):
            if(state[i] > state[j]):
                count += 1

    if(count % 2 == 0):
        return 1
    else:
        return 0

def f_dist(g_dist,state):
    h_dist = 0
    for cur_index in range(9):
        if(state[cur_index] != purpose_state[cur_index]):
            # 数码在当前状态的位置
            cur_x, cur_y = cur_index % 3, cur_index / 3
            # 数码在目标状态的索引
            pur_index = purpose_state.index(state[cur_index])
            # 数码在目标状态的位置
            pur_x, pur_y = pur_index % 3, pur_index / 3

            h_dist += abs(cur_x - pur_x) + abs(cur_y - pur_y)
    return g_dist + h_dist

def astar():
    moves = [(0, 1, 'r'), (0, -1, 'l'), (1, 0, 'd'), (-1, 0, 'u')]

    while frontier:
        dist, (current,switch) = heapq.heappop(frontier)
        if(current == purpose_state):
            # print(f'程序占用内存: {sys.getsizeof(frontier)+sys.getsizeof(reached)}byte')
            return switch
        
        index = current.index(0)
        x, y = index // 3, index % 3        
        for move in moves:
            nx, ny = x + move[0], y + move[1]
            if((0 <= nx < 3) and (0 <= ny < 3)):
                new_node = current.copy()
                new_node[index], new_node[nx * 3 + ny] = new_node[nx * 3 + ny], new_node[index]
                
                if(tuple(new_node) not in reached):
                    heapq.heappush(frontier, (f_dist(len(switch),new_node),(new_node, switch + [move[2]])))
                    reached.add(tuple(new_node))
                
    return("unsolvable")


initial_state = list(sys.stdin.readline().split())  

# 记录程序开始时间
# start_time = time.perf_counter()

for i in range(0,9):
    if(initial_state[i] == 'x'):
        initial_state[i] = 0
    initial_state[i] = int(initial_state[i])

purpose_state = [1,2,3,4,5,6,7,8,0]

if(inversions(initial_state.copy()) == 0):
    print("unsolvable")
    exit(0)

frontier = []
heapq.heappush(frontier,(f_dist(0,initial_state),(initial_state,[])))
reached = set([tuple(initial_state)])

switch = astar()
for i in switch:
    print(i,end='')
    
# # 记录程序结束时间
# end_time = time.perf_counter()

# # 计算并打印运行时间
# running_time = end_time - start_time
# print(f'程序运行时间: {running_time}秒')

