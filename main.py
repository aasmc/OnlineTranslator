from Translator import print_translations
import sys


def initialize_translation():
    args = sys.argv
    original_lang = args[1].lower()
    target_lang = args[2].lower()
    word_to_translate = args[3].lower()

    print_translations(original_lang, target_lang, word_to_translate)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    initialize_translation()
