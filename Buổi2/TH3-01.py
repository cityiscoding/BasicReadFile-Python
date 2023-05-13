import sys

# Read input data from file
with open("C:\Project_Work\VS CODE\TH1\Buổi2\GTS1c.txt", "r") as f:
    n, k = map(int, f.readline().split())
    graph = [list(map(int, f.readline().split())) for _ in range(n)]

# Define function to calculate cost of a path
def path_cost(path):
    cost = 0
    for i in range(n - 1):
        cost += graph[path[i]][path[i+1]]
    cost += graph[path[n-1]][path[0]]
    return cost

# Define function to find optimal solution using GTS1 algorithm
def tsp_gts1():
    # Initialize necessary variables
    visited = [False] * n
    path = [0] * n
    path[0] = k-1
    visited[k-1] = True
    
    # Find path through all cities
    for i in range(1, n):
        min_cost = sys.maxsize
        next_city = -1
        for j in range(n):
            if not visited[j] and graph[path[i-1]][j] < min_cost:
                min_cost = graph[path[i-1]][j]
                next_city = j
        path[i] = next_city
        visited[next_city] = True
    
    # Complete the solution by returning to the starting city
    path.append(k-1)
    
    return path_cost(path), path

# Execute the algorithm and print the result
cost, path = tsp_gts1()
print("Optimal cost:", cost)
print("Path through all cities:", path)