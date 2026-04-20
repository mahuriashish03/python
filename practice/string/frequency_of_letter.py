from collections import Counter

def frequency_of_letters(word):
    frequecy = {}
    for letter in word:
        if letter in frequecy:
            frequecy[letter] += 1
        else:
            frequecy[letter] = 1
    return frequecy

def frequency_of_letter_using_counter(word):
    return Counter(word)

def main():
    word = input("Enter the string: ")
    print(frequency_of_letters(word))
    print(frequency_of_letter_using_counter(word))

if __name__ == "__main__":
    main()