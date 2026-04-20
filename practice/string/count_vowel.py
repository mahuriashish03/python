def count_vowels(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for letter in word:
        if letter in vowels:
            count += 1
    return count

def main():
  word = input("Enter a string: ")
  print(count_vowels(word))

if __name__ == "__main__":
    main()