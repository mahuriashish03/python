def remove_spaces_from_string(word):
    result = ""
    for letter in word:
        if letter != " ":
            result+= letter
    return result

def remove_spaces_using_contains(word):
    return word.replace(" ", "")

def remove_spaces_using_join(word):
    return "".join(letter for letter in word if letter != " ")

def main():
    word = input("Enter your String:")
    print(remove_spaces_from_string(word))
    print(remove_spaces_using_contains(word))
    print(remove_spaces_using_join(word))


if __name__ == "__main__":
    main()