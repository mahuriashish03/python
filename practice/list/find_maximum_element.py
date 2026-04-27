def find_max(my_list):
    max = my_list[0]
    for element in my_list:
        if element > max:
            max = element

    return max


def main():
    my_list = [1, 2, 3, 4, 15, 6, 7, 8, 9, 10]
    print(find_max(my_list))


if __name__ == "__main__":
    main()