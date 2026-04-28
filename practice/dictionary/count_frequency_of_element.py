def count_frequency_of_element(my_list):
    frequency = {}
    for item in my_list:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1

    return frequency


def main():
    my_list = list(map(int, input("Enter your values: ").split()))
    print(count_frequency_of_element(my_list))

    my_lsit_second = input("Enter your values: ").split()
    print(count_frequency_of_element(my_lsit_second))

if __name__ == "__main__":
    main()