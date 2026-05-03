def anagram(string1, string2):
    frequency = {}
    for char in string1:
        frequency[char] = frequency.get(char, 0) + 1

    for char in string2:
        if char in frequency:
            frequency[char] = frequency.get(char, 0) - 1
        else:
            return False

    for key,value in frequency.items():
        if value != 0:
            return False

    return True

def second_largest_number(my_list):
    first = second = float("-inf")
    for item in my_list:
        if item > first:
            second = first
            first = item
        elif first > item > second:
            second = item
    return second


def most_frequency_char(string):
    frequency = {}
    maxi = 0
    char = ""
    for char in string:
        if char in frequency:
            frequency[char] = frequency.get(char, 0) + 1
        else:
            frequency[char] =  1
    for key,value in frequency.items():
        if value > maxi:
            maxi = value
            char = key
    return char



def main():

    print(anagram("aab", "ab"))
    print(second_largest_number([1, 4 , 76, 100, 4, 8]))
    print(most_frequency_char("silenttttttsss"))


if __name__ == "__main__":
    main()