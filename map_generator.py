import sys
from random import choices

def main():
    if len(sys.argv) != 2:
        print("USAGE: python map_generator.py map_name.txt")
    possibilities = ".xo"
    probabilities = [1.0, 0.12, 0.12]
    generated_map = "\n".join(["".join([choices(possibilities, weights=probabilities)[0] for _ in range(20)]) for _ in range(20)])
    with open(sys.argv[1], "w") as map_file:
        map_file.write(generated_map)

if __name__ == "__main__":
    main()
