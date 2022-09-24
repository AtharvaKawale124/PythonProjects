import random
y='yy'

while y=='y':
    x = random.randrange(1, 7)
    if x==1:
        print("-------------")
        print("|           |")
        print("|     *     |")
        print("|           |")
        print("-------------")
    elif x == 2:
        print("-------------")
        print("|           |")
        print("|   *   *   |")
        print("|           |")
        print("-------------")
    elif x == 3:
        print("-------------")
        print("|  *    *   |")
        print("|           |")
        print("|    *      |")
        print("-------------")
    elif x == 4:
        print("-------------")
        print("|  *    *   |")
        print("|           |")
        print("|  *    *   |")
        print("-------------")

    elif x == 5:
        print("-------------")
        print("|  *     *  |")
        print("|     *     |")
        print("|  *     *  |")
        print("-------------")
    elif x == 6 :
        print("-------------")
        print("|  *     *  |")
        print("|  *     *  |")
        print("|  *     *  |")
        print("-------------")
    y = input("Press y to roll aganin.")


