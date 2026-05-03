def count_vowels(string):
    count = 0
    for letter in string:
        if letter.lower() in "aeiou":
            count += 1
        else:
            pass
    return count

def main():

    user_input = input("Please insert your values: ")
    print(count_vowels(user_input))

if __name__ == "__main__":
    main()