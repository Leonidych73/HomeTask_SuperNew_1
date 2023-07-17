"""HomeTask_12.
Given list of list of integers
write recursive function that will accept as argument target list
and return sum of all integers inside it
Input: [[[[1, 4, 5], [[6, 9],[[[8, 1], 7], 3], 2], 7], 5, 2], 9, [1, 2]]
Output: Target sum = 72
"""
list_of_list = [[[[1, 4, 5], [[6, 9], [[[8, 1], 7], 3], 2], 7], 5, 2], 9, [1, 2]]  # input


def funct_sum_list(l1):
    sum_items = 0
    for itm in l1:  # iterate over elements of list
        if type(itm) is int:  # create the base case: if the element is integer then add it to sum_items
            sum_items += itm
        elif type(itm) is list:  # create the recursive case: if the element is list then call recursive function
            sum_items += funct_sum_list(itm)
    return sum_items  # return total sum


target_sum = funct_sum_list(list_of_list)
print("Target sum =", target_sum)  # print result
