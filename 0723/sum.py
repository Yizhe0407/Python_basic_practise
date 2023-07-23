# 2023/07/23
# method 1
def sum(input_list):
    length = len(input_list)
    if length <= 1:
        return input_list[0]
    else:
        return input_list[0] + sum(input_list[1:])

my_list = [5, 7, 9, 15, 21, 6]
print(f'sum = {sum(my_list)}')

# method 2
def sum_recursive(input_list):
    if not input_list:
        return 0
    else:
        return input_list[0] + sum_recursive(input_list[1:])

my_list = [5, 7, 9, 15, 21, 6]
print(f'sum = {sum_recursive(my_list)}')


# method 3
def sum_recursive_helper(input_list, index):
    if index == len(input_list) - 1:
        return input_list[index]
    else:
        return input_list[index] + sum_recursive_helper(input_list, index + 1)

def sum_recursive(input_list):
    return sum_recursive_helper(input_list, 0)

my_list = [5, 7, 9, 15, 21, 6]
print(f'sum = {sum_recursive(my_list)}')
