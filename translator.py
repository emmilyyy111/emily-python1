

def translate(phrase):
    new_word = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                new_word = new_word + "G"
            else:
                new_word = new_word + "g"
        else:
            new_word = new_word + letter
    return new_word

print(translate(input("Enter a phrase: ")))


