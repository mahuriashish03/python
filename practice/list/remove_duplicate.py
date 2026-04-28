def remove_duplicate(my_list):
    unique_list = []
    for item in my_list:
        if item not in unique_list:
            unique_list.append(item)
        else:
            pass

    return unique_list

def main():
    my_list = list(map(int, input("Insert your values: ").split()))
    print(remove_duplicate(my_list))

if __name__ == "__main__":
    main()