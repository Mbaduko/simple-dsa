def reverse_string(word):

    reversedWord = ""
    for i in range(len(word) - 1, -1, -1):
        reversedWord += word[i]
    return reversedWord

def palindrome(word):
    if len(word) <= 1:
        return True
    return word == reverse_string(word)

def count_vowels_consonants(word):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0

    for char in word:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    return vowel_count, consonant_count


user_input = input("enter a word: ")
print(palindrome(user_input))

print(count_vowels_consonants(user_input))