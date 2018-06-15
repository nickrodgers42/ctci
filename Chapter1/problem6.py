# Write a function to return a compressed string 
# by printing the first letter and the count of repeated letters

if __name__ == "__main__":
    origStr = input()
    newStr = ''
    lastChar = origStr[0]
    count = 1
    for i in range(1, len(origStr)):
        if origStr[i] == lastChar:
            count += 1
        else:
            newStr += lastChar + str(count)
            lastChar = origStr[i]
            count = 1
    newStr += lastChar + str(count)
    lastChar = origStr[i]
    print(newStr) if len(newStr) < len(origStr) else print(origStr)