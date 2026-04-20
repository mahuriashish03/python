def count_constant(word):
    count = 0
    vowels = ["a", "e", "i", "o", "u"]
    for letter in word:
        if letter not in vowels:
            count += 1
    return count


def main():
    word = input("Input the string:")
    print(count_constant(word))

if __name__ == "__main__":
    main()