def find_min(my_list):
    minimum = my_list[0]

    for element in my_list:
        if element < minimum:
            minimum = element

    return minimum

def main():
    my_list = list(map(int, input("Insert your values: ").split()))
    print(find_min(my_list))

if __name__ == "__main__":
    main()