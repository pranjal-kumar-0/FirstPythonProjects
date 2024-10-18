def second_largest_num(list_of_nums):
    unique_list = list(set(list_of_nums))
    unique_list.remove(max(unique_list))
    return max(unique_list)
