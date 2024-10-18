def largest_num(nums: list):
    max_num = nums[0]
    for i in nums:
        if i > max_num:
            max_num = i

    return max_num
