import random

money = 100
wins = 0
loses = 0

while money > 0:
    print(" Số tiền hiện tại:", money, "$")
    comp_number = random.randint(1, 100)

    level = int(input("Chọn level [1: dễ, 2: vừa, 3: khó]: "))
    if level == 1:
        times = 10
    elif level == 2:
        times = 5
    else:
        times = 3

    win = False
    for i in range(times):
        guess = int(input("Nhập số bạn đoán #" + str(i+1) + ": "))

        if guess == comp_number:
            print(" Chính xác! Bạn thắng ")
            win = True
            break
        elif guess < comp_number:
            print(" Số bạn đoán nhỏ quá!")
        else:
            print(" Số bạn đoán lớn quá!")

    if win:
        wins += 1
    else:
        loses += 1
        money -= 5

        print(" Bạn thua! Số đúng là:", comp_number)

    print("📊 Kết quả: Thắng =", wins, ", Thua =", loses, ", Tiền =", money, "$")

    if money <= 0:
        print("💸 Bạn đã hết tiền! Game over!")
        break

    cont = input("Bạn có muốn chơi tiếp không? (y/n): ")
    if cont.lower() == "n":
        break

print("\nCảm ơn bạn đã chơi game 🎮")