import sys

def compress_coordinates(n):
    nums = list(map(int, sys.stdin.readline().split()))
    sortednums = sorted(set(nums))
    worddict = {num : count for count, num in enumerate(sortednums)}
    print(' '.join(str(worddict[element]) for element in nums))

if __name__ == "__main__":
    compress_coordinates(int(sys.stdin.readline()))
