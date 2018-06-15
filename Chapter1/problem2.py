# Given two strings, write a method to determine if one is a permutation of the other

# The runtime of this problem is O(a + b) because we have to go through each string. We are assuming a O(1) insertion and retrieval from the dictionary

# The other way that the book recommended going about this probem was to first compare the lengths of the strings, sort the strings
# and then iterate through them to compare that. 
# Given an O(nlog(n)) runtime for sorting, I think that would come out to a runtime of O(nlog(n) + nlog(n) + n), or just O(nlog(n))

def isPerm(str1, str2):
    if (len(str1) != len(str2)):
        return False
    str1Dict = {}
    for i in range(len(str1)):
        if (str1[i] in str1Dict):
            str1Dict[str1[i]] += 1
        else:
            str1Dict[str1[i]] = 1
    for i in range(len(str2)):
        if (str2[i] in str1Dict):
            str1Dict[str2[i]] -= 1
            if (str1Dict[str2[i]] <= 0):
                del str1Dict[str2[i]]
        else:
            return False
    return True

if __name__ == "__main__":
    inputStrings = input().split()
    str1 = inputStrings[0]
    str2 = inputStrings[1]
    permutation = isPerm(str1, str2)
    if permutation:
        print(str1 + " is a permutation of " + str2)
    else:
        print(str1 + " is not a permutation of " + str2)