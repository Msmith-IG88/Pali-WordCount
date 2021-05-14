def count(s):
    count = 0
    if type(s) != str:
        return "Invalid Input" 
    for i in s:
        if i == ' ':
            count = count + 1
    return count + 1
