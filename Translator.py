import requests
from bs4 import BeautifulSoup

language_map = {
    "en": "english",
    "fr": "french"
}

supported_languages = [
    "Arabic",
    "German",
    "English",
    "Spanish",
    "French",
    "Hebrew",
    "Japanese",
    "Dutch",
    "Polish",
    "Portuguese",
    "Romanian",
    "Russian",
    "Turkish"
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
    while not response.status_code == 200:
        response = requests.get(url, headers=headers)
    return response.content


def print_translations(original_number, target_number, word):
    original = supported_languages[original_number - 1].lower()
    target = supported_languages[target_number - 1].lower()
    content = get_content_page(original, target, word)
    soup = BeautifulSoup(content, 'html.parser')
    translation_links = soup.find_all('a', {
        'class': ['translation', 'dict'],
    })
    translations = []
    for link in translation_links:
        to_add = link.text.strip()
        if to_add and to_add != "Translation":
            translations.append(to_add)
    sources = soup.find_all('div', {'class': 'src'})
    source_sentences = []
    for s in sources:
        sentence = s.text.strip()
        if sentence:
            source_sentences.append(sentence)
    targets = soup.find_all('div', {'class': 'trg'})
    target_sentences = []
    for t in targets:
        t_sentence = t.text.strip()
        if t_sentence:
            target_sentences.append(t_sentence)
    result_sentences = []
    for i in range(0, len(source_sentences)):
        result_sentences.append(source_sentences[i])
        result_sentences.append(target_sentences[i])
    target_language = target.capitalize()
    print(f"\n{target_language} Translations:")
    for translation in translations:
        print(translation)
    print(f"\n{target_language} Examples:")
    for i in range(0, len(result_sentences)):
        if i > 0 and i % 2 == 0:
            print(f"\n{result_sentences[i]}")
        else:
            print(result_sentences[i])
