number= input('Enter a number:')
number.split()
nums = []

for x in number:
    nums.append(x)

for i in range(0, len(nums)):
    for j in range(0, len(nums)-1):
        if nums[j] < nums[j+1]:
            nums[j], nums[j+1] = nums[j+1],nums[j]
                                                
answer = int(''.join(nums))


print(answer)