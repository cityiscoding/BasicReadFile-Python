import math
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

# Đọc dữ liệu từ file
with open("array2.txt", "r") as f:
    m, n = map(int, f.readline().split())
    # Đọc các phần tử trong mảng
    a = []
    for i in range(m):
        row = list(map(int, f.readline().split()))
        a.append(row)

# Mở file để ghi kết quả
with open("array2.out", "w") as f:
    # Đếm số lượng số nguyên tố
    count = 0
    for i in range(m):
        for j in range(n):
            if is_prime(a[i][j]):
                count += 1
    f.write("So luong so nguyen to: {}\n".format(count))

    # Tính tổng từng dòng
    for i in range(m):
        row_sum = sum(a[i])
        f.write("Tong cua dong {}: {}\n".format(i+1, row_sum))

    # Tính tổng từng cột
    for j in range(n):
        col_sum = sum(a[i][j] for i in range(m))
        f.write("Tong cua cot {}: {}\n".format(j+1, col_sum))
