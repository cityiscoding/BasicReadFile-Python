import math
import time
import itertools

# Đọc file input và tạo ma trận trọng số c
def read_input_file(file_path):
    with open(file_path, 'r') as f:
        n, m = map(int, f.readline().strip().split())
        distances = []
        for i in range(n):
            row = list(map(int, f.readline().strip().split()))
            distances.append(row)
    return n, m, distances


# Hàm tính chi phí của một hành trình
def compute_cost(path, c):
    cost = 0
    for i in range(len(path) - 1):
        cost += c[path[i]][path[i+1]]
    cost += c[path[-1]][path[0]]
    return cost


# Hàm tìm đường đi ngắn nhất bằng thuật toán GTS2
def gts2_tsp(n, c):
    # Khởi tạo biến
    start_time = time.time()
    best_cost = float('inf')
    best_path = []
    path = [0]

    # Lặp lại cho đến khi không còn cải tiến được
    for _ in range(math.factorial(n-1)):
        for perm in itertools.permutations(range(1, n)):
            curr_path = path + list(perm) + [0]
            cost = compute_cost(curr_path, c)
            if cost < best_cost:
                best_cost = cost
                best_path = curr_path[:]
        path = best_path[:-1]

    # In kết quả và thời gian chạy thuật toán
    print("Best cost:", best_cost)
    print("Best path:", best_path)
    print("Time:", time.time() - start_time)


# Thực hiện chương trình
n, m, distances = read_input_file("C:\Project_Work\VS CODE\TH1\Buổi2\GTS2a.txt")
gts2_tsp(n, distances)
