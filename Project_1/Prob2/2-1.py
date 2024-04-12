import queue
import sys 
# import time

moves = [3,-3,1,-1]    

def find_neighbor(state):
    index = state.index(0)
    for move in moves:
        neighbor = state.copy()           
        #移动后的位置是否还在九宫格内
        if(0 <= index + move < 9 and (index % 3 != 0 or move != -1) and (index % 3 != 2 or move != 1)):
            neighbor[index], neighbor[index + move] = neighbor[index + move], neighbor[index]

            state1 = tuple(state)
            neighbor1 = tuple(neighbor)
            depth_state = reached[state1]+1
            if(neighbor1 not in reached or depth_state < reached[neighbor1]):    #深度更浅
                reached[neighbor1] = depth_state
                stack.put(neighbor1)

initial_state = list(sys.stdin.readline().split())  

# 记录程序开始时间
# start_time = time.perf_counter()

for i in range(0,9):
    if(initial_state[i] == 'x'):
        initial_state[i] = 0
    else:
        initial_state[i] = int(initial_state[i])  
initial_state = tuple(initial_state)  

purpose_state = (1,2,3,4,5,6,7,8,0)

# 后入先出队列
stack = queue.LifoQueue()
stack.put(initial_state)

reached = {} 
reached[initial_state] = 1

max_layers = 50

while True:
    if stack.empty():
        print(0)
        exit(0)

    stack_top = stack.get(block=True, timeout=None)

    if(stack_top == purpose_state):  
        print(1)
        # 记录程序结束时间
        #end_time = time.perf_counter()

        # 计算并打印运行时间
        # running_time = end_time - start_time
        # print(f'程序运行时间: {running_time}秒')
        # print(f'程序占用内存: {sys.getsizeof(stack)+sys.getsizeof(reached)}byte')
        exit(0)
    if(reached[stack_top] < max_layers):   
        find_neighbor(list(stack_top))   

