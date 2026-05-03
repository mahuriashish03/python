def find_max(my_list):
    maximum = my_list[0]
    for item in my_list:
        if item > maximum:
            maximum = item
    return maximum

def main():
    user_input = [1,4,6,9,1,4,3]
    print(find_max(user_input))

if __name__ == "__main__":
    main()