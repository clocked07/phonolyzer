import pickle

sef = open('files/env.dat', 'rb')
sound_env = pickle.load(sef)

phef = open('files/phonemes.dat', 'rb')
phonemes  = pickle.load(phef)

sef.close()
phef.close()

allophones = dict()

for sound in sound_env:
    if sound not in phonemes:
        for phoneme in phonemes:
            if sound_env[sound].isdisjoint(sound_env[phoneme]): #the two never occur in same env, ie they are in complementary distribution
                try:
                    allophones[phoneme].add(sound)
                except:
                    allophones[phoneme] = {sound}

outf = open('files/allophones.dat', 'wb')
pickle.dump(allophones, outf)

print("Phoneme \tPossible Allophones\n")
for phoneme in allophones:
    print(f"{phoneme} \t{allophones[phoneme]}")

