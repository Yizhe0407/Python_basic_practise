# 2023/07/13
# 九九乘法表
for j in range(1,10):
    for k in range(1,10):
        result = j * k
        print(f"{j} * {k} = {result:<3d}", end = "  ")
    print()