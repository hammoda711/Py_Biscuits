def my_function(my_list_1):
    my_list_1 = [5, 7]
    print("Print #1:", my_list_1)
    print("Print #2:", my_list_2)
    del my_list_1[0]  # Pay attention to this line.
    print("Print #3:", my_list_1)
    print("Print #4:", my_list_2)

my_list_1 = [5, 7]
my_list_2 = [2, 3]
my_function(my_list_2)
print("Print #5:", my_list_2)
'''
def my_function(my_list_1):
    print("Print #1:", my_list_1)
    print("Print #2:", my_list_2)
    del my_list_1[0]  # Pay attention to this line.
    print("Print #3:", my_list_1)
    print("Print #4:", my_list_2)


my_list_2 = [2, 3]
my_function(my_list_2)
print("Print #5:", my_list_2)


'''
'''
he key point here is that both my_list_1 and my_list_2 refer to the same list object. Modifying the list through one of the references (in this case, my_list_1) will be reflected in the other reference (my_list_2).
'''



