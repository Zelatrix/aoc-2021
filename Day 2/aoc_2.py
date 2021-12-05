'''
Calculate the final position of the submarine, when it started
from the origin in Cartesian co-ordinates

@param puzzle the planned course for the submarine
@return the product of the final horizontal position and final depth
'''

def solve(puzzle):
    
    horizontal = 0
    depth = 0

    splitted = puzzle
    # print(splitted)
    i = 0
    while i < len(splitted)-1:
        if splitted[i] == "forward":
            horizontal += int(splitted[i+1].strip())
            i += 2
            # print(horizontal, depth)
        elif splitted[i] == "down":
            depth += int(splitted[i+1].strip())
            i += 2
            # print(horizontal, depth)
        elif splitted[i] == "up":
            depth -= int(splitted[i+1].strip())
            i += 2
            # print(horizontal, depth)
    return horizontal * depth

def main():
    with open("aoc_2.txt") as puzzle:
        pz = [p.strip().split(" ") for p in puzzle.readlines()]
        flat = [y for x in pz for y in x]
        print(solve(flat))

if __name__ == "__main__":
    main()

