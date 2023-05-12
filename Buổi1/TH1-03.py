import random

n = 100000  # Số lượng số cần tạo ra
filename = "array1.txt"  # Tên file để lưu trữ

# Tạo một danh sách chứa n số ngẫu nhiên trong phạm vi từ 1 đến 100
numbers = [random.randint(1, 100) for i in range(n)]

# Ghi danh sách số vào file
with open(filename, 'w') as f:
    f.write(str(n) + '\n')  # Ghi số lượng số vào dòng đầu tiên
    for i in range(0, n, 10):
        f.write(' '.join(str(x) for x in numbers[i:i+10]) + '\n')  # Ghi 10 số vào mỗi dòng tiếp theo
