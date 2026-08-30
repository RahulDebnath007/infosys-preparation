line = input().strip()
nums = list(map(int, line.split()))

i4 = nums.index(4)
i7 = nums.index(7)

sum_before = sum(nums[:i4])
sum_after = sum(nums[i7+1:])
concat_num = int("".join(str(x) for x in nums[i4:i7+1]))

result = sum_before + sum_after + concat_num
print(result)