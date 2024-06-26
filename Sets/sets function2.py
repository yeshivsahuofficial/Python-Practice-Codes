my_set = {1, 2, 3, 4, 5}
my_set2 = {2, 5, 6, 7, 8}

union_set = my_set.union(my_set2)
print(union_set)
#     OR
# union_set = my_set | (my_set2)
# print(union_set)

difference_set = my_set.difference(my_set2)     # my_set-my_set2
print(difference_set)

intersection_set = my_set.intersection(my_set2)
print(intersection_set)
