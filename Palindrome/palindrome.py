def pal(w):
    if type(w) != str:
        return "Invalid Input"
    if w[:] == w[::-1]:
        return "Is Palindrome"
    else:
        return "Not Palindrome"
