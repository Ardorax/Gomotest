#!/usr/bin/python3
from io import IOBase
import sys
import os

Stone = tuple[int, int]
Stones = list[Stone]

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    GREY = '\033[36m'


def printer(text: str, file: IOBase):
    print(text)
    x = input()
    file.write(f"->{text}\n<-{x}\n")
    return x

def readMap(filePath: str) -> tuple[Stones, Stones, Stones]:
    lineCount = 0
    player = []
    opponant = []
    output = []
    with open(filePath, "r") as file:
        for line in file:
            for i, char in enumerate(line):
                if char == "x":
                    player.append((i, lineCount))
                elif char == "o":
                    opponant.append((i, lineCount))
                elif char == "@":
                    output.append((i, lineCount))
            lineCount += 1
    return (player, opponant, output)

def convertToBoard(player : Stones, oppoant : Stones) -> str:
    res = "BOARD\n"
    for stone in player:
        res += f"{stone[0]} {stone[1]} 1\n"
    for stone in oppoant:
        res += f"{stone[0]} {stone[1]} 2\n"
    return res + "DONE"

def test(testMapPath: str, file: IOBase) -> bool:
    printer("START 20", file)
    player, opponant, sol = readMap(testMapPath)
    out = printer(convertToBoard(player, opponant), file).split(",")
    out = (int(out[0]), int(out[1]))
    if out not in sol:
        print(f"{bcolors.FAIL}ERROR file: {testMapPath}{bcolors.ENDC}", file=sys.stderr)
        for y in range(20):
            for x in range(20):
                if (x, y) in sol:
                    print(f"{bcolors.OKCYAN}@{bcolors.ENDC}", end="", file=sys.stderr)
                elif (x, y) in player:
                    print(f"x", end="", file=sys.stderr)
                elif (x, y) in opponant:
                    print(f"o", end="", file=sys.stderr)
                elif (x, y) == out:
                    print(f"{bcolors.FAIL}Y{bcolors.ENDC}", end="", file=sys.stderr)
                else:
                    print(".", end="", file=sys.stderr)
            print(file=sys.stderr)
        return False
    else:
        print(f"{bcolors.OKGREEN}OK file : {testMapPath} Play : {out}{bcolors.ENDC}", file=sys.stderr)
        return True

def main():
    with open("log.txt", "w") as log:
        for filePath in os.listdir("map"):
            test(f"map/{filePath}", log)

    print("END")
    log.close()

if __name__ == "__main__":
    main()