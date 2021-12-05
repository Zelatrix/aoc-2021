'''
The puzzle comes in the form of an array of integers
and we need to determine whether or not the numbers
increase

@param puzzle - the array of integers
@return count - the number of times the previous number is less than the next number along
'''
def solve(puzzle):
    index = 0
    count = 0

    while index < len(puzzle)-1:
        if puzzle[index] < puzzle[index+1]:
            count += 1
            index += 1
        else:
            index += 1
    return count

def main():
    with open("aoc_1.txt") as puzzle:
        l = []
        for line in puzzle.readlines():
            l.append(int(line.strip()))
        print(solve(l))

if __name__ == "__main__":
    main()
