#!/usr/bin/python3
import sys

def createMap() -> list[list[int]]:
    map = []
    for i in range(0, 20):
        map.append([])
        for j in range(0, 20):
            map[i].append(0)
    return map

def displayMap(map: list[list[int]]):
    for i in range(0, 20):
        for j in range(0, 20):
            if map[i][j] == 1:
                print("x", end="")
            elif map[i][j] == 2:
                print("o", end="")
            else:
                print(".", end="")
        print()

def main():
    map = createMap()
    displayMap(map)
    with open(sys.argv[1], "r") as file:
        for line in file:
            x, y, player = line.split(",")
            x = int(x)
            y = int(y)
            map[x][y] = int(player)
            displayMap(map)
            input()

if __name__ == "__main__":
    main()