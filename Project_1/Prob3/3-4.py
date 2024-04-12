import heapq 
import sys

path = {}
path[(0,0)] = [(0,0)]

def f_dist(g_dist,node):
    h_dist = (n-1-node[0]) + (m-1-node[1])
    f_dist = g_dist + h_dist
    return f_dist

def astar():      
    global min_path
    global shortest_path
    
    while frontier:
        depth, (x,y) = heapq.heappop(frontier)
        if (x,y) == (n-1,m-1):
            min_path = depth
            shortest_path = path[(x,y)]
            print(min_path)
            return shortest_path
                
        neighbors = find_neighbors(x,y)
        path_state = path[(x,y)]     
        for nx, ny in neighbors:
            if(maze[nx][ny] == 0):
                neighbor = (nx,ny)
                depth_state = f_dist(len(path_state), neighbor)
                if neighbor not in reached:
                    reached.add(neighbor)
                    path[neighbor] = path_state + [(nx, ny)]
                    heapq.heappush(frontier, (depth_state, neighbor))
    
def find_neighbors(i, j):
    neighbors = []
    if(i > 0): neighbors.append((i-1,j))
    if(i < n-1): neighbors.append((i+1,j)) 
    if(j > 0): neighbors.append((i,j-1))
    if(j < m-1): neighbors.append((i,j+1))
    return neighbors

n,m = map(int, sys.stdin.readline().split())

maze = []
for i in range(0,n):
    maze.append(list(map(int, input().split())))
    
frontier = []
heapq.heappush(frontier,(0,(0,0)))
reached = set([(0,0)])
    
min_path = float('inf')
shortest_path = []

astar()