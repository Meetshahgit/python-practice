# this a simple translator which shows how to use nested loops and build a simple translator 
# ps: this translator doesnt translate to any known langauge 
# this translator which replace vovals letter to help it translate to very own unique language

def translate(phrase):
    translatation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translatation = translatation + "P"
            else:
                translatation = translatation + "p"
        else:
            translatation = translatation + letter
    return translatation

print(translate(input("Enter a Phrase: ")))