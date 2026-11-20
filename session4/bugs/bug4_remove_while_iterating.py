# Find the bug 4: never change the list you are looping over. Build a new one
nums = [1, 2, 2, 3, 4]
nums = [n for n in nums if n % 2 != 0]
print(nums)
