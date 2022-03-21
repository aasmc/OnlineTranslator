from Translator import print_translations


def initialize_translation():
    print(
        'Type "en" if you want to translate from French into English, or "fr" if you want to translate from English '
        'into French:')
    target = input()
    original = "en" if target == "fr" else "fr"
    print("Type the word you want to translate:")
    word = input()
    output = f'You chose {target} as a language to translate "{word}.'
    print(output)
    print_translations(original, target, word)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    initialize_translation()
