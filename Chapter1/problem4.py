# Check if a string is a permutation of a palindrome.

# For this problem I would have had to ask the interviewer
# what is considered a palindrome, as the book was not counting spaces
# Additionally, there was a /slightly/ more optimized solution
# Which negated the need for a second for loop

def isPalindrome(palString):
    palString.lower()
    strChars = {}
    for i in range(len(palString)):
        if (ord(palString[i]) >= 97 and ord(palString[i]) <= 122):
            if (palString[i] in strChars):
                strChars[palString[i]] += 1
                strChars[palString[i]] %= 2
            else:
                strChars[palString[i]] = 1
    numOdd = 0
    for i in strChars:
        if strChars[i] == 1:
            numOdd += 1
            if (numOdd > 1):
                return False
    return True

def improvedIsPalindrome(palString):
    palString.lower()
    strChars = {}
    numOdd = 0
    for i in range(len(palString)):
        if (ord(palString[i]) >= 97 and ord(palString[i]) <= 122):
            if (palString[i] in strChars):
                strChars[palString[i]] += 1
                strChars[palString[i]] %= 2
                numOdd -=1
            else:
                strChars[palString[i]] = 1
                numOdd += 1
    return numOdd <= 1


if __name__ == "__main__":
    palindromeStr = input()
    if (improvedIsPalindrome(palindromeStr)):
        print("This string is a permutation of a palindrome")
    else:
        print("This string is not a permutation of a palindrome")