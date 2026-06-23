def reverse_string(word):

    reversedWord = ""
    for i in range(len(word) - 1, -1, -1):
        reversedWord += word[i]
    return reversedWord

def palindrome(word):
    if len(word) <= 1:
        return True
    return word == reverse_string(word)


user_inout = input("enter a word: ")
print(palindrome(user_inout))