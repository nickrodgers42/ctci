# Write a function to replace the spaces in a string with "%200"
# Input is in the form "<string>     ", <length> where the string is long enough to contain all of the characters and replaced spaces

# This has an O(n) runtime, since we just have to run through the length of the string

# This gets the job done, but I think the book was looking for a way that was more focused on a character array

if __name__ == "__main__":
    inputStr = input()
    urlStr = inputStr.split(',')[0][1:-1]
    urlStr = urlStr.strip()
    url = ""
    for i in range(len(urlStr)):
        if (urlStr[i] == ' '):
            url += "%20"
        else:
            url += urlStr[i]
    print('"' + url + '"')