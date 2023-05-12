import random

m = int(input("Nhap gia tri cua m: "))
n = int(input("Nhap gia tri cua n: "))

with open("array2.txt", "w") as f:
    f.write(str(m) + " " + str(n) + "\n")
    for i in range(m):
        row = " ".join(str(random.randint(1, 100)) for j in range(n))
        f.write(row + "\n")

print("Da tao file array2.txt thanh cong.")
