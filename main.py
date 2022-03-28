from Translator import print_translations
from Translator import print_supported_languages


def initialize_translation():
    print("Hello, welcome to the translator. Translator supports:")
    print_supported_languages()
    print("Type the number of your language:")
    original_number = int(input())
    print("Type the number of a language you want to translate to or '0' to translate to all languages:")
    target_number = int(input())
    print("Type the word you want to translate:")
    word = input()
    print_translations(original_number, target_number, word)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    initialize_translation()
