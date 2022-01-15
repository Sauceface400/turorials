def translator(Phrase):
    translator = ""
    for letters in Phrase: 
        if letters.lower() in "aeiou": #Or letters in "AEIOUaeiou"
            if letters.isupper():
                translator = translator + "G"
            else:
                translator = translator + "g"
        else:
            translator = translator + letters
    return translator
print(translator(input("Enter text: ")))