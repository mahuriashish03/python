def replace_vowels_with_stars(word):
    vowels = "aeiouAEIOU"
    result = ""
    for letter in word:
        if letter in vowels:
            result += "*"
        else:
            result += letter

    return result

def main():
    word = input("Enter your word: ")
    print(replace_vowels_with_stars(word))


if __name__ == "__main__":
    main()