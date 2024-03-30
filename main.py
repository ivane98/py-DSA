# Given a 0-indexed integer array nums of length n and an integer target, return the number of pairs (i, j) where 0 <= i < j < n and nums[i] + nums[j] < target.

# solution loop through the list twice and append matching tuples to the list and return the length of that list

def count_pairs(nums, target):
    res = []
    for i in range(len(nums)):
        for j in range(1, len(nums)):
            if (nums[i] + nums[j]) < target:
                if i < j:
                    res.append((i, j))
    return len(res)

nums = [-6,2,5,-2,-7,-1,3]

print(count_pairs(nums, -2))