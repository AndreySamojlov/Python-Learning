def string_expect (str1, str2):
    if type(str1) == str and type(str2) == str:
        if str1 == str2:
            return 1
        elif len(str1) > len(str2):
            return 2
        elif str2 == "learn":
            return 3
    else:
        return 0
print(string_expect ('str1', 1)) #0
print(string_expect ('str1', 'str1')) #1
print(string_expect ('str1', '1')) #2
print(string_expect ('str1', 'learn')) #3