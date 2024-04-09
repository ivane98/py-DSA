import os

# a generic binary search
def binary_search(data, target, low, high):
    if low > high:
        return False
    else:
        mid = (low + high)//2
        if data[mid] == target:
            return True
        elif data[mid] < target:
            return binary_search(data, target, mid + 1, high)
        else:
            return binary_search(data, target, low, mid - 1)
        

# calculates total amount of disk space in kbs for entire directory and its subdirectories
def disk_usage(path):
    total = os.path.getsize(path)

    if os.path.isdir(path):
        for filename in os.listdir(path):
            childpath = os.path.join(path, filename)
            total += disk_usage(childpath)
    return total


def power(x, n):
    if n ==0:
        return 1
    else:
        print(n)
        return x * power(x, n-1)
    





