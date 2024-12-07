# [1, 2, 3, 4, 5, 6] => [[1, 2, 3], [4, 5, 6]]
my_list_1 = [1, 2, 3, 4, 5, 6]
half_1 = (len(my_list_1) + 1) // 2
result_1 = [my_list_1[:half_1], my_list_1[half_1:]]
print(my_list_1 , "=>", result_1)

# [1, 2, 3, 4, 5] => [[1, 2, 3], [4, 5]]
my_list_2 = [1, 2, 3, 4, 5]
half_2 = (len(my_list_2) + 1) // 2
result_2 = [my_list_2[:half_2], my_list_2[half_2:]]
print(my_list_2 , "=>", result_2)

# [] => [[], []]
my_list_3 = []
half_3 = (len(my_list_3) + 1) // 2
result_3 = [my_list_3[:half_3], my_list_3[half_3:]]
print(my_list_3 , "=>", result_3)