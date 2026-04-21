def find_first_unique_char(word):
    size = len(word)
    for i in range(len(word)):
        count = 0
        for j in range(size):
            if word[j] == word[i]:
                count += 1
        if count == 1:
            return word[i]
    return None


def find_first_unique_char_using_dic(word):
    dictionary = {}
    for letter in word:
        if letter in dictionary:
            dictionary[letter] += 1
        else:
            dictionary[letter] = 1

    for key, value in dictionary.items():
        if value == 1:
            return key
    return None


def main():
    word = input("Input your string: ")
    print(find_first_unique_char(word))
    print(find_first_unique_char_using_dic(word))

if __name__ == "__main__":
    main()