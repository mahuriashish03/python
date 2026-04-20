from collections import Counter
def string_anagram(word1, word2):
    word1 = word1.lower().replace(" ", "")
    word2 = word2.lower().replace(" ", "")
    my_list = list(word1)
    #Time complexity : O(n**2)
    for letter in word2:
        if letter in my_list:
            my_list.remove(letter)
        else:
            return False
    return len(my_list) == 0

def check_anagram_using_sorted(word1, word2):
    #Time complexity = O(n log n)
    return sorted(word1.lower().replace(" ", "")) == sorted(word2.lower().replace(" ", ""))

def check_anagram_using_counter(word1, word2):
    #Time complexity = O(n)
    return Counter(word1.lower().replace(" ", "")) == Counter(word2.lower().replace(" ", ""))

def main():
    word = input("Enter first word: ")
    word2 = input("Enter second word: ")
    print(string_anagram(word, word2))
    print(check_anagram_using_sorted(word, word2))
    print(check_anagram_using_counter(word, word2))

if __name__ =="__main__":
    main()