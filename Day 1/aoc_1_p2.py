def solve(puzzle):
     i = 0
     j = 0
     count = 0
     while i < len(puzzle): 
        window_1 = puzzle[i:i+3]
        w1_sum = sum(window_1)
        window_2 = puzzle[j:j+3]
        w2_sum = sum(window_2)   
        
        if w1_sum < w2_sum:
            count += 1
        i += 1
        j += 1

        if len(window_1) == 3:
            pass
        elif len(window_2) == 3:
            pass
        else:
            break
     return count

        #print(window_2)
        #print(w2_sum)

def main():
    with open("aoc_tmp.txt") as puzzle:
        l = []
        for line in puzzle.readlines():
            l.append(int(line.strip()))
        print(solve(l))

main()
