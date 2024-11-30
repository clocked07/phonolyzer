f = open('files/ipa_words.txt', 'r', encoding='utf-8')
wrf = open('files/minimal_pairs.txt', 'w', encoding='utf-8')
import unicodedata

def get_char(word):
    word = unicodedata.normalize('NFC', word)
    pastletter = word[0]
    for letter in word:
        if unicodedata.combining(letter) or letter in ['ʰ', 'ː', '\u032A']:
            pastletter += letter
        else:
            yield pastletter
            pastletter = letter
    yield pastletter
    yield None

words = []
for line in f.readlines():
    line = line.strip()
    if line != '':
        words.append(line)


found = set()
for i in range(len(words)):
    for j in range(i+1, len(words)):
        word1 = words[i]
        word2 = words[j]
        if word1 == word2:
            continue
        diffs = 0
        diffchars = ['NULL', 'NULL']
        if len(word1) == len(word2):
            letters1 = get_char(word1)
            letters2 = get_char(word2)
            letter1 = True
            letter2 = True
            while (letter1 is not None) and (letter2 is not None):
                letter1 = next(letters1)
                letter2 = next(letters2)
                if letter1 != letter2:
                    diffchars[0] = letter1
                    diffchars[1] = letter2
                    diffs += 1
                    if diffs > 1:
                        break
            if diffs <= 1 and (word1, word2) not in found:
                print(f"{word1} {word2} {diffchars[0]} {diffchars[1]}")
                wrf.write(f"{word1} {word2} {diffchars[0]} {diffchars[1]}\n")
                found.add((word1, word2))

            
        

