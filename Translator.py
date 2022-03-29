import requests
from bs4 import BeautifulSoup

language_map = {
    "en": "english",
    "fr": "french"
}

supported_languages = [
    "arabic",
    "german",
    "english",
    "spanish",
    "french",
    "hebrew",
    "japanese",
    "dutch",
    "polish",
    "portuguese",
    "romanian",
    "russian",
    "turkish"
]


def print_supported_languages():
    for i in range(0, len(supported_languages)):
        print(f"{i + 1}. {supported_languages[i]}")


base_url = "https://context.reverso.net/translation/"


def form_url(original, target, word):
    url = f"{base_url}{original}-{target}/{word}"
    return url


def get_content_page(original, target, word):
    url = form_url(original, target, word)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    return response


def get_translations(_soup):
    translation_links = _soup.find_all('a', {
        'class': ['translation', 'dict'],
    })
    translations = []
    for link in translation_links:
        to_add = link.text.strip()
        if to_add and to_add != "Translation":
            translations.append(to_add)
    return translations


def get_source_sentences(_soup):
    sources = _soup.find_all('div', {'class': 'src'})
    source_sentences = []
    for s in sources:
        sentence = s.text.strip()
        if sentence:
            source_sentences.append(sentence)
    return source_sentences


def get_target_sentences(_soup):
    targets = _soup.find_all('div', {'class': 'trg'})
    target_sentences = []
    for t in targets:
        t_sentence = t.text.strip()
        if t_sentence:
            target_sentences.append(t_sentence)
    return target_sentences


def get_result_sentences(sources, targets):
    result_sentences = []
    for i in range(0, len(sources)):
        result_sentences.append(sources[i])
        result_sentences.append(targets[i])
    return result_sentences


def print_result(target_language, translations, result_sentences, is_file_created, word):
    mode = "a" if is_file_created else "w"
    with open(f"{word}.txt", mode) as f:
        translation_phrase = f"\n{target_language.capitalize()} Translations:"
        print(translation_phrase)
        translation_phrase = translation_phrase if is_file_created else translation_phrase[1:]
        f.write(translation_phrase + "\n")
        for translation in translations:
            print(translation)
            f.write(translation + "\n")
        example_phrase = f"\n{target_language} Examples:"
        print(example_phrase)
        f.write(example_phrase + "\n")
        for i in range(0, len(result_sentences)):
            if i > 0 and i % 2 == 0:
                to_print = f"\n{result_sentences[i]}"
                print(to_print)
                f.write(to_print + "\n")
            else:
                print(result_sentences[i])
                f.write(result_sentences[i] + "\n")


def print_single_language(page_content, target, is_file_created, word):
    soup = BeautifulSoup(page_content, 'html.parser')

    translations = get_translations(soup)
    source_sentences = get_source_sentences(soup)
    target_sentences = get_target_sentences(soup)
    result_sentences = get_result_sentences(source_sentences, target_sentences)
    target_language = target.capitalize()
    print_result(target_language, translations[0:1], result_sentences[0:2], is_file_created, word)


def print_translations(original, target, word):
    if original not in supported_languages:
        print(f"Sorry, the program doesn't support {original}")
    elif target != "all" and target not in supported_languages:
        print(f"Sorry, the program doesn't support {target}")
    elif target != "all":
        response = get_content_page(original, target, word)
        if response.status_code == 200:
            print_single_language(response.content, target, False, word)
        elif response.status_code == 404:
            print(f"Sorry, unable to find {word}")
        else:
            print("Something wrong with your internet connection")
    else:
        index = 0
        for lang in supported_languages:
            if lang != original:
                response = get_content_page(original, lang, word)
                if response.status_code == 200:
                    print_single_language(response.content, lang, index != 0, word)
                elif response.status_code == 404:
                    print(f"Sorry, unable to find {word}")
                    break
                else:
                    print("Something wrong with your internet connection")
                index += 1
