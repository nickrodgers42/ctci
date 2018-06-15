# Check if two strings are only one edit away

def oneAway(str1, str2):
    if (abs(len(str1) - len(str2)) > 1):
        return False
    else:
        numDif = 0
        if (max(len(str1), len(str2)) == len(str1)):
            for i in range(len(str2)):
                if (str1[i] != str2[i]):
                    numDif += 1
                    if numDif > 1:
                        return False
        else:
            for i in range(len(str1)):
                if (str1[i] != str2[i]):
                    numDif += 1
                    if numDif > 1:
                        return False
    return True

if __name__ == "__main__":
    str1 = input()
    str2 = input()
    print("The strings are one away") if oneAway(str1,str2) else print("The strings are not one away") 