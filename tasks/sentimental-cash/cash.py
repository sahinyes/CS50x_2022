from cs50 import get_float


coins = 0

#Controlling input
while True:
    cents = get_float("Change Owed: ")
    if cents >= 0:
        break
    else:
        print("Invalid input, type another number")

#Counting coins
cents = cents * 100

while cents >= 25:
    cents = cents - 25
    coins += 1
while cents >= 10:
    cents = cents - 10
    coins += 1
while cents >= 5:
    cents = cents - 5
    coins += 1
while cents >= 1:
    cents = cents - 1
    coins += 1
print(coins)
