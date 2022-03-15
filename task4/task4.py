import sys
import numpy as np

def calc_min_dist(nums):

    nums_sort = sorted(nums.copy())
    median = nums_sort[len(nums) // 2]
    min_dist = np.sum([abs(x - median) for x in nums_sort])
    return min_dist

def main():

    with open(sys.argv[1], "r") as nums_file:

        nums = list(map(int, nums_file.read().split('\n')))
        min_dist = calc_min_dist(nums)
        print(min_dist)


if __name__ == '__main__':
    main()