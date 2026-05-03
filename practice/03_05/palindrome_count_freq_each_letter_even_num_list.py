def palindrome(string):
    if string == "":
        return None
    rever_string = string[::-1]

    return rever_string == string

def frequeny_of_char(string):
    if string == "":
        return None
    frequency = {}
    for char in string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    return frequency

def even_num_list(my_list):
    if not my_list:
        return None
    even_list = []
    for num in my_list:
        if num %2 == 0:
            even_list.append(num)

    return even_list


def main():

    string = input("Please enter the string: ")
    print(palindrome(string))
    print(frequeny_of_char(string))

    my_list = list(map(int, input("Please enter the number: ").split()))
    print(even_num_list(my_list))

if __name__ == "__main__":
    main()