# Given 2 strings, find out if string 2 is a rotation of string 1 
# using only 1 call to isSubstring

# This question was not too difficult but it took me a long time to realize how to implement it
# (I looked at the hints in the book)

# The book also checks if the strings are not empty and are the same length, 
# which I forgot on the first time

def isSubstring(str1, str2):
    return str2 in str1

if __name__ == "__main__":
    str1 = input()
    str2 = input()

    if len(str1) > 0 and len(str1) == len(str2):
        origStr2 = str2
        str2 += str2
        if isSubstring(str2, str1):
            print(origStr2 + " is a rotation of " + str1)
        else:
            print(origStr2 + " is not a rotation of " + str1)
    else:
        print(origStr2 + " is not a rotation of " + str1)
        