vowels = list("aeiou")
def convert(string):
    if string == "quit!":
        return
    if len(string) > 4 and string[-1] == "r" and string[-2] == "o" and string[-3] not in vowels:
        return string.replace("or", "our")
    else:
        return string

string = ""
while string != "quit!":
    string = input()
    if convert(string):
        print(convert(string))
