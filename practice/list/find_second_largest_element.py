def find_second_largest_element(my_list):
    if len(my_list) < 2:
        return None

    first = second = float("-inf")
    for item in my_list:
        if item > first:
            second = first
            first = item
        elif first > item > second:
            second = item
    return second


def main():
    my_list = list(map(int, input("Insert your values: ").split()))
    print(find_second_largest_element(my_list))

if __name__ == "__main__":
    main()