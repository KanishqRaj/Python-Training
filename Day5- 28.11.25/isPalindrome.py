def isPalindrome(words):
    words = words.lower()
    return words == words[::-1]

word = input("Enter a string: ")
if isPalindrome(word):
    print("Palindrome")
else:
    print("Not Palindrome")