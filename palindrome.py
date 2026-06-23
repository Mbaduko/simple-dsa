def palindrome(word):
    if len(word) <= 1:
        return True
    reversedWord = ""
    for i in range(len(word) - 1, -1, -1):
        reversedWord += word[i]
    return word == reversedWord


user_inout = input("enter a word: ")
print(palindrome(user_inout))