nums = input("числа через пробіл: ").split()

for i in range(len(nums)):
    nums[i] = float(nums[i])

for i in range(len(nums)):
    for j in range(len(nums)-i-1):
        if nums[j] > nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]

print("відсортовано:", nums)
