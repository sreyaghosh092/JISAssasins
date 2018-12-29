def remove_vowel(string):
    vowels=('a','e','i','o','u')
    for x in string.lower():
        for x in vowels:
            string=string.replace(x," ")
    print(string)
string=input(print("Enter a sentence: "))
new_string=remove_vowel(string)
