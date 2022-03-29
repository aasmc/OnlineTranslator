# Online Translator

Educational project from HyperSkill Academy Python Core track, level hard. 

## Stage 2
## Objectives

At this stage, your program should:

- Take an input specifying the target language (en if the user wants to translate from French into English, or fr if the user wants to translate from English into French).
- Take an input specifying the word that should be translated.
- Output the confirmation message in the format You chose "..." as a language to translate "...".
- Form a request and connect to ReversoContext.
- Check the HTTP status of the response of the website https://context.reverso.net/translation/ to your request. If the status code is 200, you are good to proceed! If not... Try again?
- Output the response of the website to your request (200) and OK message to show that the connection is successful (so, the entire line should be 200 OK).
- Output the line Translations.
- Output a list with translations of the given word in the target language: ['bonjour', 'salut'].
- Output a list with examples of sentences featuring the given word or any of its translations: ['Well, hello, freedom fighters.', 'Et bien, bonjour combattants de la liberté.']. Both the original versions of the sentences and their translations should be printed. You don't need to filter sentences in any way: just print all the sentences that ReversoContext output for the given language pair and the given word.

Make sure you output exactly the sentences that ReversoContext shows initially on the page https://context.reverso.net/translation/{language_1}-{language_2}/{word}. Don't confound them with the sentences that the website shows when you click on the first translation equivalent. These sentences will not be accepted by tests.

Also, please, make sure your program follows the described format of the output.
### Example

The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

```text
Type "en" if you want to translate from French into English, or "fr" if you want to translate from English into French:
> fr
Type the word you want to translate:
> hello
You chose "fr" as a language to translate "hello".
200 OK
Translations
['bonjour', 'allô', 'ohé', 'coucou', 'salut', 'hello', 'bonsoir', "quelqu'un", 'bien le bonjour', 'Oh', 'Enchanté', 'saluer', 'ça', 'salue', 'Oui']
['Well, hello, freedom fighters.', 'Et bien, bonjour combattants de la liberté.', 'Goodbye England and hello the Netherlands...', "Au revoir l'Angleterre et bonjour les Pays-Bas...", 'Yes, hello. Jackson speaking.', "Oui, allô, Jackson à l'appareil.", 'Hello, hello, hello, hello.', 'Allô, allô, allô, allô.', 'And began appearing hello kitty games online.', 'Et a commencé à apparaître bonjour Kitty jeux en ligne.', 'Tell him hello... and congratulations.', 'Je lui dis bonjour et je le félicite.', 'A special hello to everyone from YouTube Bibi.', 'Un bonjour spécial à tout le monde de la chaîne de beauté YouTube de bibi.', 'Yes, hello, Mr Teodoresco.', 'Oui, bonjour, M. Teodoresco.', 'Well hello, Milan and Eve.', 'Eh bien bonjour, Milan et Eve.', 'Well hello, welcome to the Tree House pond.', "Alors bonjour, bienvenue à l'étang de la Maison de l'arbre.", 'pink hello kitty seat 2,3 - Auto Outlet', 'rose bonjour 2,3 siège de minou - Auto Outlet', 'hello world PL/SQL procedure successfully completed. SQL', 'bonjour procédure monde PL / SQL terminée avec succès. SQL', '"Maido-san" means something like "hello" in Kanazawa dialect.', 'Maido-sans veut dire quelque chose comme bonjour dans le dialecte de Kanazawa.', 'So anyway, hello and goodbye.', 'Donc voilà, bonjour et au revoir.', 'You can hardly hear him saying hello.', "On l'entend à peine dire bonjour.", "Yes, hello. I'd like to blackmail the Prime Minister.", "Oui, bonjour, j'aimerais faire chanter le premier Ministre.", 'Well, please tell her hello for us.', 'Bien, dites lui bonjour de notre part.', 'Homie, I think someone is saying hello.', "Homer, je crois qu'on te dit bonjour.", 'Well, hello, Susan and welcome.', 'Bien, bonjour Susan et bienvenue.', 'Normally, one says "hello" only once.', 'Normalement, on dit bonjour une fois.']
```

## Stage 3
Objectives

At this stage, format the output of results in the following fashion:

- Output the line ... Translations:; put the full name of the target language instead of ... (for example, English Translations).
- Output found translations, one per line. Make sure there are no commas or quotes, just the word (or the phrase). If there are more than 5 translations, leave only 5 of them to keep the results more compact. Or you can print all of them, it does not affect the testing.
- Output the line ... Examples; put the full name of the target language instead of ... .
- Output found examples of sentences, one sentence per line. Make sure there are no commas or quotes (apart from those that should be inside the sentence). First, output the sentence in the source language, then output its translation in the target language. Repeat this procedure for every found sentence pair. If there are more than 5 sentence pairs, you can leave only 5 of them for convenience. Or you can print all of them, it does not affect the testing.

### Example

The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

```text
Type "en" if you want to translate from French into English, or "fr" if you want to translate from English into French:
> fr
Type the word you want to translate:
> hello
You chose "fr" as a language to translate "hello".
200 OK

French Translations:
bonjour
allô
ohé
coucou
salut

French Examples:
Well, hello, freedom fighters.
Et bien, bonjour combattants de la liberté.

Goodbye England and hello the Netherlands...
Au revoir l'Angleterre et bonjour les Pays-Bas...

Yes, hello. Jackson speaking.
Oui, allô, Jackson à l'appareil.

Hello, hello, hello, hello.
Allô, allô, allô, allô.

And began appearing hello kitty games online.
Et a commencé à apparaître bonjour Kitty jeux en ligne.
```

## Stage 4

### Description

Great job! You now have a basic translation app that works well. Wouldn’t it be great though to expand it and include all available languages? This will finally make our translator a multilingual one!

The maximum number of languages our translator can support is 13. They are:

- Arabic
- German
- English
- Spanish
- French
- Hebrew
- Japanese
- Dutch
- Polish
- Portuguese
- Romanian
- Russian
- Turkish

They should be enumerated in the program. A great idea is to present them with relevant numbers so that the user can choose the first as the original language and the second as a translation.
Objectives

At this stage, your program should:

- Output the welcoming message (let's update it a bit): Hello, welcome to the translator. Translator supports:
- Output an enumerated list of languages. The enumeration should start from 1. The order of languages should be exactly as in the list above.
- Take input (a number from the list) specifying the source language (the language from which the translation should be performed).
- Take input (a number from the list) specifying the target language (the language to which the translation should be performed).
- Take input specifying the word that should be translated.
- Output the results as in the previous stage. At this stage, you don't need to print 200 OK anymore.

Tip 1: just place the listed languages into the URL depending on the user’s choice!

Tip 2: Try to convert the input to lower case: it may cause an error if the user's input is in upper case or mixed.
### Example

The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

```text
Hello, welcome to the translator. Translator supports: 
1. Arabic
2. German
3. English
4. Spanish
5. French
6. Hebrew
7. Japanese
8. Dutch
9. Polish
10. Portuguese
11. Romanian
12. Russian
13. Turkish
Type the number of your language: 
> 3
Type the number of language you want to translate to: 
> 4
Type the word you want to translate:
> hello

Spanish Translations:
hola
buenos días
qué tal
saludo
buen día

Spanish Examples:
Well, hello, Miss Anchor-liar.:
Bien, hola, señorita presentadora de mentiras.

He didn't introduce us, so hello.:
No nos presentó, así que hola.

Well, hello, Prince Charming.:
Vaya, hola, Príncipe Azul.

In addition, fast delivery. hello Laura.:
Además, la entrega rápida. hola Laura.

L: Well, hello, my dear secretary.:
A: Bien, hola, mi querida secretaria.
```

## Stage 5
### Description

Perfect! Your program already became a convenient tool. There are just a couple of stages left. Your translation app is flexible enough to be appreciated by many people worldwide, so let's make it even better: add the feature of translating the word to all the languages at once, and also save the search results to a text file so that the user could read the translations later.
### Objectives

Add the following functionality to your program:

- Before taking an input specifying the target language, output the message Type the number of a language you want to translate to or '0' to translate to all languages:
- If the user inputs 0 as the target language, translate the word to all available languages.
- Output results to the terminal, as in the previous stage. At this stage, it's enough to print just one translation and one sentence pair per target language.
- Save results of the search to a file named word.txt, where word is the word that was being translated.

### Example

The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.
```text
Hello, welcome to the translator. Translator supports: 
1. Arabic
2. German
3. English
4. Spanish
5. French
6. Hebrew
7. Japanese
8. Dutch
9. Polish
10. Portuguese
11. Romanian
12. Russian
13. Turkish
Type the number of your language:
> 3
Type the number of a language you want to translate to or '0' to translate to all languages:
> 0
Type the word you want to translate:
> hello
```
This will result in the following output and a file called hello.txt with the same content:
```text
Arabic Translations:
مرحبا

Arabic Example:
Well, hello, old-school racist.:
حسنا، مرحبا يا تلميذة المدرسة العنصريّة - الأمر يسري بدمهم!


German Translations:
hallo

German Example:
We agreedellen wolf is innocent. hello.:
Wir waren einverstanden damit, dass Wolf unschuldig ist. Hallo.


Spanish Translations:
hola

Spanish Example:
Well, hello, Miss Anchor-liar.:
Bien, hola, señorita presentadora de mentiras.


French Translations:
bonjour

French Example:
Well, hello, freedom fighters.:
Et bien, bonjour combattants de la liberté.


Hebrew Translations:
שלום

Hebrew Example:
Is "hello" too bland?:
האם "שלום" יותר מדי מנומס?


Japanese Translations:
こんにちは

Japanese Example:
The little boy said hello to me.:
小さな男の子が私にこんにちはと言った。


Dutch Translations:
dag

Dutch Example:
That was kind of our funny hello.:
Dat vond we een grappige begroeting.


Polish Translations:
cześć

Polish Example:
I guess it's... goodbye car insurance, hello city bus.:
I domyślam się, że to jest... do widzenia ubezpieczenie samochodu, cześć autobus miejski.


Portuguese Translations:
olá

Portuguese Example:
That was my last kiss hello.:
Pois eu garanto que aquele foi o meu último beijo de olá.


Romanian Translations:
salut

Romanian Example:
Well, hello, professor Culbertson.:
Ei bine, salut, profesor universitar Culbertson.


Russian Translations:
привет

Russian Example:
Why, hello, there, Admiral.:
А, Адмирал, привет, что здесь делаешь.


Turkish Translations:
selam

Turkish Example:
So now little Sabina says hello.:
Velhasıl minik Sabina size selam söylüyor.
```
## Stage 6
### Description

Let's try to change the way the user interacts with the program to make the process faster. To make your program more convenient, you can use command-line arguments. They make it possible to provide a program with all the data it needs using a simple command.
### Objectives

At this stage, your program should:

- Instead of all inputs, take command-line arguments. The first argument is the name of the source language, the second argument is the name of the target language, the third argument is the word. If the word should be translated to all languages, the second argument will be all.
- The rest of the functionality should remain the same as in the previous stage.

You'll see some significant changes in the usability of the app!
### Examples

The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

### Example 1

You can choose the number of translations and sentence pairs for a language. There should be just at least one translation and one sentence pair.
```text
> python translator.py english french hello
French Translations:
bonjour
allô
ohé
coucou
salut

French Examples:
Well, hello, freedom fighters.:
Et bien, bonjour combattants de la liberté.

Goodbye England and hello the Netherlands...:
Au revoir l'Angleterre et bonjour les Pays-Bas...

Yes, hello. Jackson speaking.:
Oui, allô, Jackson à l'appareil.

Hello, hello, hello, hello.:
Allô, allô, allô, allô.

And began appearing hello kitty games online.:
Et a commencé à apparaître bonjour Kitty jeux en ligne.
```

### Example 2
```text
> python translator.py english all hello
Arabic Translations:
مرحبا

Arabic Example:
Well, hello, old-school racist.:
حسنا، مرحبا يا تلميذة المدرسة العنصريّة - الأمر يسري بدمهم!


German Translations:
hallo

German Example:
We agreedellen wolf is innocent. hello.:
Wir waren einverstanden damit, dass Wolf unschuldig ist. Hallo.


Spanish Translations:
hola

Spanish Example:
Well, hello, Miss Anchor-liar.:
Bien, hola, señorita presentadora de mentiras.


French Translations:
bonjour

French Example:
Well, hello, freedom fighters.:
Et bien, bonjour combattants de la liberté.


Hebrew Translations:
שלום

Hebrew Example:
Is "hello" too bland?:
האם "שלום" יותר מדי מנומס?


Japanese Translations:
こんにちは

Japanese Example:
The little boy said hello to me.:
小さな男の子が私にこんにちはと言った。


Dutch Translations:
dag

Dutch Example:
That was kind of our funny hello.:
Dat vond we een grappige begroeting.


Polish Translations:
cześć

Polish Example:
I guess it's... goodbye car insurance, hello city bus.:
I domyślam się, że to jest... do widzenia ubezpieczenie samochodu, cześć autobus miejski.


Portuguese Translations:
olá

Portuguese Example:
That was my last kiss hello.:
Pois eu garanto que aquele foi o meu último beijo de olá.


Romanian Translations:
salut

Romanian Example:
Well, hello, professor Culbertson.:
Ei bine, salut, profesor universitar Culbertson.


Russian Translations:
привет

Russian Example:
Why, hello, there, Admiral.:
А, Адмирал, привет, что здесь делаешь.


Turkish Translations:
selam

Turkish Example:
So now little Sabina says hello.:
Velhasıl minik Sabina size selam söylüyor.
```

## Stage 7
### Description

Your program works as expected! However, there’s a problem you should always keep in mind: the user can always input something that will break your program.

Up to this stage, we considered "perfect" inputs. But what if things go wrong? For example, you gave your program to someone who’s not familiar with the concept behind it. What if they try to translate to or from languages different from those you have in your code, or even start typing jabberwocky? Let's find some way to avoid this.

All these situations are called exceptions because you didn’t expect them to happen, and now your program will have to handle them.
### Objectives

Add the following functionality:

- If the user inputs a name of a language that isn't available in the program, print the line Sorry, the program doesn't support <language> and quit the program.
- If the connection with the website isn't successful, print the line Something wrong with your internet connection
- If the user inputs a word that's not present in ReversoContext, print the line Sorry, unable to find <word>

### Examples

The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

```text
> python translator.py english korean hello
Sorry, the program doesn't support korean
```

```text
> python translator.py english all hello
Something wrong with your internet connection
```

```text
> python translator.py english all brrrrrrrrrrr
Sorry, unable to find brrrrrrrrrrr
```