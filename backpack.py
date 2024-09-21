def print_backpack(backpack):
    for a in backpack:
        print("       ".join(list(map(str, a))))
    print()

def theft(product, backpack, S):
    if S < 0:
        return 0
    max_value = 0
    index = -1
    
    for i in range(len(product)):
        if S - product[i][0] >= 0:
            temp = backpack[S - product[i][0]][0] + product[i][1]
            if max_value < temp:
                max_value = temp
                index = i
        elif i == 0:
            return 0

    backpack[S][0] += max_value

    for i in range(1, len(product) + 1):
        backpack[S][i] = backpack[S - product[index][0]][i]

    backpack[S][index + 1] += 1
    print_backpack(backpack)
    return backpack[S][0]


def main():
    S = 20
    product = [
        [3, 5],
        [4, 7],
        [5, 10]
    ]
    backpack = [[0] * 4 for _ in range(S + 1)]

    for i in range(S + 1):
        theft(product, backpack, i)

    for j in range(4):
        print(backpack[S][j], end=" ")
    print()


if __name__ == "__main__":
    main()
