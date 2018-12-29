def remove_a(string):
    toremove=('a')
    for x in string.lower():
        for x in toremove:
            string=string.replace(x," ")
    print(string)
string=input(print("Enter a sentence: "))
new_string=remove_a(string)