ans = 30
guess = 0
figure = 0
while(figure != ans):
    figure = int(input("請猜1~100間的數字 = "))
    guess += 1
    if figure > ans:
        print("請猜小一點")
    elif figure == ans:
        print("恭喜答對了")
        break
    else:
        print("請猜大一點")
print(f"共猜 {guess} 次")