def merge_sorted_lists(list1, list2):
    merged_list = []
    for i in list1:
        merged_list.append(i)
    for i in list2:
        merged_list.append(i)
    merged_list.sort()
    return merged_list

