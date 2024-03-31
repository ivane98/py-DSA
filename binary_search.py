def binary_search(lo, hi, condition):

    while lo <= hi:

        mid = (lo + hi) // 2
        result = condition(mid)

        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        else:
            lo = mid + 1

    return -1

def first_position(nums, target):
    def condition(mid):
        if nums[mid] == target:
            if mid > 0 and nums[mid-1] == target:
                return 'left'
            return 'found'
        elif nums[mid] < target:
            return 'right'
        else:
            return 'left'
    return binary_search(0, len(nums)-1, condition)

def last_position(nums, target):
    def condition(mid):
        if nums[mid] == target:
            if mid < len(nums)-1 and nums[mid+1] == target:
                return 'right'
            return 'found'
        elif nums[mid] < target:
            return 'right'
        else:
            return 'left'
    return binary_search(0, len(nums)-1, condition)

def first_and_last_position(nums, target):
    return first_position(nums, target), last_position(nums, target)
   

cards = [1, 2, 3, 4, 5, 6, 7, 8, 8, 9]

print(first_and_last_position(cards, 8))

# given a rotated list determine how many times has it been rotated from the sorted list

# example inputs and outputs: [5, 6, 9, 0, 2, 3, 4] out put is 3 becose original list was [0, 2, 3, 4, 5, 6, 9]

# solution: sort the list first and save it in a variable. then start poping elements and append them to the front of the list after every iteration compare to the sorted list and count then return count

def count_rotations(nums):
    s_nums = sorted(nums)
    count = 0

    while s_nums != nums:
        last = s_nums[-1]
        s_nums.pop()
        s_nums.insert(0, last)
        count += 1
    return count

def count_rotations_binary(nums):
    lo = 0
    hi = len(nums) - 1
    
    while lo <= hi:
        mid = (lo + hi) // 2             
        if mid > 0 and nums[mid] < nums[mid - 1]:
            return mid
        elif nums[mid] < nums[-1]:
            hi = mid - 1  
        else:
            lo = mid + 1

nums = [19, 25, 29, 3, 5, 6, 7, 9, 11, 14]

print(count_rotations_binary(nums))







