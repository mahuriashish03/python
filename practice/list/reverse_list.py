def reverse_list(my_list):
    new_list = []

    for element in range(len(my_list) -1 , -1, -1):
        new_list.append(my_list[element])
    return new_list

def reverse_list_using_slicing(my_list):
    return my_list[::-1]

def reverse_list_using_reverse_method(my_list):
    my_list.reverse()
    return my_list

def main():
    my_list = list(map(int, input("Insert the list value").split()))
    print(reverse_list(my_list))
    print(reverse_list_using_slicing(my_list))
    print(reverse_list_using_reverse_method(my_list))

if __name__ == "__main__":
    main()