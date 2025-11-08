# Brute Force Approach O(n^2)
def brute_find(s, n):
    list_size = len(s)
    for i in range(list_size):
        for j in range(i+1,list_size):
            if s[i] + s[j] == n:
                return f"{i},{j}"

# Optimized approach - Idea is that i definitely only want to use one for loop
def find(s, n):
    # So instead of a second loop we will use a different data strucutre that allows 
    # for easeier retrieval in faster O time
    # Python dicts are hashmaps
        nums_hashed = {}
        index = 0
        for num in nums :
            nums_hashed[num] = nums_hashed.get(num, index)
            index += 1

        list_size = len(nums)
        for i in range(list_size):
            remainder = target - nums[i]
            if remainder in nums_hashed and i != nums_hashed[remainder]:
                return [i,nums_hashed[remainder]]



nums = [2,7,11,15]
target = 9

print(find(nums, target))


