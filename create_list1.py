def create_list(input_1, input_2):
    new_list = []
    new_list.append(input_1)
    new_list.append(input_2)
    new_list.append(input_1)
    return new_list

def adjust_list(a, b):
    my_list = set(create_list(a, b))
    print(my_list)

adjust_list('red', 'blue')