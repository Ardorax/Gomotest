#!/usr/bin/python3
import sys
from main import bcolors

def createMap() -> list[list[int]]:
    map = []
    for i in range(0, 20):
        map.append([])
        for j in range(0, 20):
            map[i].append(0)
    return map

def displayMap(map: list[list[int]], player : int):
    for i in range(0, 20):
        for j in range(0, 20):
            if map[i][j] == 1:
                print("x", end="")
            elif map[i][j] == 2:
                print("o", end="")
            elif map[i][j] == 3:
                print(f"{bcolors.BOLD}{bcolors.OKGREEN}X{bcolors.ENDC}", end="")
                if player == 2:
                    map[i][j] = 1
            elif map[i][j] == 4:
                print(f"{bcolors.BOLD}{bcolors.FAIL}O{bcolors.ENDC}", end="")
                if player == 1:
                    map[i][j] = 2
            else:
                print(".", end="")
        print()

def main():
    map = createMap()
    with open(sys.argv[1], "r") as file:
        for i, line in enumerate(file):
            x, y, player = line.split(",")
            x = int(x)
            y = int(y)
            player = int(player)
            map[x][y] = player + 2
            input(f"Coup {i + 1}:")
            displayMap(map, player)

if __name__ == "__main__":
    main()