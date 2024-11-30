#program to find environment in which all sounds in the dataset occur. used after extract_phonemes.py to prepare data for use in find_allophones.py
import unicodedata
def get_char(word):
    word = unicodedata.normalize('NFC', word)
    pastletter = ""
    for letter in word:
        if unicodedata.combining(letter) or letter in ['ʰ', 'ː', '\u032A'] or pastletter == "":
            pastletter += letter
        else:
            yield pastletter
            pastletter = letter
    yield pastletter

sound_env = dict()

f = open('files/ipa_words.txt', 'r', encoding='utf-8')

words = []

line = f.readline()
while line:
    line = line.strip()
    if line != '':
        words.append(line)
    line = f.readline()


for word in words:
    word = list(get_char(word))

    for i in range(len(word)):
        if i == 0 and len(word) != 1:
            env = "#_" + word[i+1]
        elif i == len(word) - 1:
            env = word[i-1] + "_#"
        else:
            env = word[i-1] + "_" + word[i+1]
        letter = word[i]
        if letter == 't':
            print(word)
        try:
            sound_env[letter].add(env)
        except:
            sound_env[letter] = {env}
        # print(f"{word}:{letter}:{env}")


# print phoneme envs first 

import pickle
phfile = open('files/phonemes.dat', 'rb')
phonemes = pickle.load(phfile)
# print(phonemes)
print("------- KNOWN PHONEMES --------")
for phoneme in phonemes:
    print(f"/{phoneme}/: ", sound_env[phoneme])


print("\n\n--------- POSSIBLE ALLOPHONES -----------")

for sound in sound_env:
    if sound not in phonemes:
        print(f"/{sound}/: ", sound_env[sound])

dump = open('files/env.dat', 'wb')
pickle.dump(sound_env, dump)