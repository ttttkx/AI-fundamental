import queue
import sys

reached = {}
path = {}
moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def dfs(state):
    for dx,dy in moves:
        #移动是否合法
        nx, ny = state[0]+dx, state[1]+dy
        if(0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 0):
            neighbor = (nx,ny)
            depth_state = reached[state]+1
            
            if(neighbor not in reached or depth_state < reached[neighbor]):    #深度更浅
                reached[neighbor] = depth_state
                path[neighbor] = path[state] + [(nx, ny)]
                stack.put(neighbor)


n,m = map(int, sys.stdin.readline().split())

maze = []
for i in range(0,n):
    maze.append(list(map(int, sys.stdin.readline().split())))

stack = queue.LifoQueue()
stack.put((0,0))
reached[(0,0)] = 0
path[(0,0)] = [(0,0)]

max_layers = 100
min_path = float('inf')
shortest_path = []

while not stack.empty():
    stack_top = stack.get(block=True, timeout=None)

    if(stack_top == (n-1,m-1)):
        if reached[stack_top] < min_path:
            min_path = reached[stack_top]
            shortest_path = path[stack_top]
            
    if(reached[stack_top] < max_layers):
        dfs(stack_top)

print(min_path)

