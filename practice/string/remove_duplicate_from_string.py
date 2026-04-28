def remove_duplicate(string):
    my_list = []
    # O(n**2)
    for item in string:
        if item not in my_list:
            my_list.append(item)
        else:
            pass

    return "".join(my_list)

def remove_duplicate_using_dics(string):
    #O(n)
    return "".join(dict.fromkeys(string))

def main():
    string = input("Enter a string: ")
    print(remove_duplicate(string))

if __name__ == "__main__":
    main()