def compare(slice1, slice2):
    count = 0
    if sum(slice1) < sum(slice2):
        count += 1
    return count

def solve(puzzle):
    i = 0
    j = 0
    count = 0

    while j < len(puzzle)-1:
        window_1 = puzzle[i:i+3]
        # i += 1
        window_2 = puzzle[i+1:i+4]
        i += 1
        j += 1

        if len(window_1) == 3:
            # print(window_1, sum(window_1))
            if sum(window_1) < sum(window_2):
                count += 1
        elif len(window_2) == 3:
            # print(window_2, sum(window_2))
            if sum(window_1) < sum(window_2):
                count += 1
    return count

def main():
    with open("aoc_1.txt") as puzzle:
        l = []
        for line in puzzle.readlines():
            l.append(int(line.strip()))
        print(solve(l))

main()
