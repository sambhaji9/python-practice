def black_white(my_list):
    new_list = []
    for item in my_list:
        if item % 2 == 0:
            new_list.append('black')
        else:
            new_list.append('white')
    print(new_list)

list = [1, 2, 3]

black_white(list)