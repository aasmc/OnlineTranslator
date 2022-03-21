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