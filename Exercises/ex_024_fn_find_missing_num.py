#sum of n terms = (n(n+1))/2  1,3

def missing_num(list_of_nums):
    starting_num = min(list_of_nums)
    ending_num = max(list_of_nums)
    actual_sum_of_list = sum(list_of_nums)
    sum1 = (starting_num * (starting_num + 1)) / 2
    sum2 = (ending_num * (ending_num + 1)) / 2
    sum_of_list = sum2 - sum1 + 1
    return int(sum_of_list - actual_sum_of_list)


print(missing_num([1, 2, 3, 5, 6]))
