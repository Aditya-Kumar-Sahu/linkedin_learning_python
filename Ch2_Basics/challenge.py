"""Program to find if given string is a pallindrome or not"""
def is_palindrome(teststr):
    # use the slice trick to reverse the string
    if teststr == teststr[::-1]:
        return True
    return False

if __name__ == '__main__':
    run = True
    while (run):
        teststr = input("Enter string to test for palindrome or 'exit':")

        # If the user types "exit" then quit the program
        if teststr == "exit":
            run = False
            break

        # convert the string to all lower case
        teststr = teststr.lower()

        # strip all the spaces and punctuation from the string
        newstr = ""
        for x in teststr:
            if x.isalnum():
                newstr += x

        print("Palindrome test:", is_palindrome(newstr))
