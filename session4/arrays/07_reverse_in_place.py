# Exercise: reverse a list in place with two pointers. O(n) time, O(1) extra memory


def reverse_in_place(lst):
    left, right = 0, len(lst) - 1
    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1


nums = [1, 2, 3, 4, 5]
reverse_in_place(nums)
print(nums)
