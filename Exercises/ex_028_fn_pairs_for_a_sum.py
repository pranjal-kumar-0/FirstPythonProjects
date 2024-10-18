# Write a Python function that finds
# all unique pairs of numbers in a list that sum up to a given target.

def pairs_for_a_sum(list_of_nums, given_sum):
    pairs = []
    for first_num in list_of_nums:
        list_of_nums.remove(first_num)
        second_num = given_sum - first_num
        if second_num in list_of_nums:
            pairs.append((first_num, second_num),)
    return pairs
