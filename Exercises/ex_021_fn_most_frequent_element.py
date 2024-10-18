def most_frequent_element(lst):
    count = 0
    frequent_element = lst[0]
    for element in lst:
        x = lst.count(str(element).lower())
        if x > count:
            count = x
            frequent_element = element

    return frequent_element
