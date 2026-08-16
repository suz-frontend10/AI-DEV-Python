def palindrome(s):
    s = s.lower()
    s = s.replace(" ", "")
    left = 0
    right = len(s) - 1
    while left < right:

        if s[left] != s[right]:
            return False
        left = left + 1
        right = right - 1
    return True
print(palindrome("madam"))
print(palindrome("Never odd or even"))
print(palindrome("python"))
print(palindrome("Was it a car or a cat I saw"))