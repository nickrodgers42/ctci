# Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?

# Complexity of this solution: O(n)

# IF I could not use additional data structures I can have an O(n^2) runtime
# by comparing each character to all the other ones. 

if __name__ == "__main__":
    cont = True
    while (cont):
        print("Enter a string to see if it has unique characters extended ascii characters.")
        stringToCheck = input()
        uniqueChars = [True for i in range(0, 256)]
        isUnique = True
        for i in range(len(stringToCheck)):
            if uniqueChars[ord(stringToCheck[i])]:
                uniqueChars[ord(stringToCheck[i])] = False
            else:
                isUnique = False
                break
        if isUnique:
            print("This string is made up of unique characters")
        else:
            print("This string is not made up of unique characters")
        print("Would you like to continue (y/n)?")

        resp = input()
        if (len(resp) > 0 and not (resp[0] == 'y' or resp[0] == 'Y')):
            cont = False