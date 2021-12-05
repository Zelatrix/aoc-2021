def get_gamma(nums, i, j):
  ones, zeroes = 0, 0
  # i, j = 0, 0
  while i < len(nums):
    if nums[i][j] == '0':
      zeroes += 1
    elif nums[i][j] == '1':
      ones += 1
    i += 1
  j += 1
  return (zeroes, ones)

# tup[0] = zeroes
# tup[1] = ones
def max_pair(tup):
  for item in tup:
    if tup[0] > tup[1]:
      return 0
    else:
      return 1

def min_pair(tup):
  for item in tup:
    if tup[0] < tup[1]:
      return 0
    else:
      return 1

def bin_to_dec(number):
  idx = 0
  res = 0
  for digit in number[::-1]:
    if digit == '1':
      res += (2**idx)
      idx += 1
    elif digit == '0':
      idx += 1
  return res

def solve(puzzle):
  gamma = ""
  epsilon = ""
  for k in range(len(puzzle[0])):
    gamma += str(max_pair(get_gamma(puzzle, 0, k)))
    epsilon += str(min_pair(get_gamma(puzzle, 0, k)))
  return bin_to_dec(gamma) * bin_to_dec(epsilon)

def main():
  # print(bin_to_dec('10110'))
  with open("aoc_3.txt") as puzzle:
    print(solve(puzzle.read().splitlines()))

main()
