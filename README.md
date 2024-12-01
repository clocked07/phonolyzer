# Phonolyzer

## About

This project is a set of programs that allows you to 

- find minimal pairs in a dataset & hence find phonemes
- find the environment every sound occurs in
- find possible allophones of the phonemes in your dataset

This code is designed to work with IPA and roman text. It has not been tested with other scripts.

It has been specially designed to work with combining characters like diatrics, superscripts, tildas, etc. 
I.e, ɑ̃ː is considered to be one sound during the analysis, not three separate characters.
Instructions regarding editing which characters are considered during this merge are given below.

## Prerequisites

- Python 3
- [Unicodedata Library](https://docs.python.org/3/library/unicodedata.html) (usually pre-installed)

## Usage

The project has 4 programs, to be executed in the following order:

1. `minimal_pairs.py`
2. `extract_phonemes.py`
3. `find_env.py`
4. `find_allophones.py`

The `files/` directory contains text & binary files generated and used by these 4 scripts. 
Examine the text files in this repository to understand their format.

### 1. `minimal_pairs.py`

The first step in analysis is identifying minimal pairs, and we use this program to do that. 
Place a text file with the words in your dataset (each separated by a newline) in `files/ipa_words.txt`.

Example of format:

```
t̪eːɾeː
bəkəɾõː
kiː
t̪oː
bɪɾəjɑːn̪iː
...
```
Empty lines are ok.

Now upon executing 

```
python minimal_pairs.py
```
You should find that a new file has been created: `files/minimal_pairs.txt`, with data in the following format:

```
t̪eːɾeː t̪eːɾiː eː iː
kiː kɑː iː ɑː
kiː ɦiː k ɦ
kiː keː iː eː
kiː koː iː oː
kiː liː k l
t̪oː t̪uː oː uː
t̪oː s̪oː t̪ s̪
...
```

Observe that the format is `Word1 Word2 Word1-Word2 Word2-Word1`. Obviously, as they are minimal pairs, `Word1-Word2` and `Word2-Word1` are single sounds.

The same text is printed to `stdout` with a slight modification: it is printed as `{word1} & {word2} & {Word1-Word2} & {Word2-Word1} \\\\`. This makes it easier to copy into a LateX table.

As mentioned before, 
> I.e, ɑ̃ː is considered as one sound during analysis, not three separate characters.

If you want to edit which sounds are combined into one during this analysis, edit this line in `minimal_pairs.py`

```
if unicodedata.combining(letter) or letter in ['ʰ', 'ː', '\u032A'] or pastletter == "":
```

### 2. `extract_phonemes.py`

This program, when run, identifies phonemes using the data in `files/minimal_pairs.txt`. 
The set of phonemes is printed to `stdout` and the same set is stored in `files/phonemes.dat`.

Example Output:

```
{'m', 'l', 'oː', 'j', 'ɪ', 'ɛ̃', 's̪', 'd̪', 'ə', 'ʋ', 'ʈ', 'u', 'b', 'ɾ', 'k', 'p', 'ɑː', 'n̪', 'bʰ', 'ɦ', 'kʰ', 't̪', 'uː', 'ɑ̃ː', 'eː', 'ĩː', 'iː'}
```

### 3. `find_env.py`

**If you modified the combining statement (`if unicodedata.combining(letter)....`) in `minimal_pairs.py` then modify it here as well.**

This script reads from `files/ipa_words.txt` and creates a map (dict) from `sound -> set of environments`.
In simpler terms, it identifies the environment (previous and next letter) that each sound in the dataset occurs in.

Environments of phonemes are printed to `stdout` before allophones'. To recognize phonemes, the program must load the set of phonemes from `files/phonemes.dat`.

Example output:

```
------- KNOWN PHONEMES --------
/t̪/:  {'s̪_ɑː', '#_iː', 'ɑː_ə', 'ɑː_eː', 'ʃ_eː', 'ɪ_ɑː', 'oː_ɑː', '#_oː', 'k_ə', '#_eː', 'ə_ɑː', 'ə_ə', '#_ə', 'oː_eː', 'ə_iː', '#_u', 'ɪ_ə', '#_uː', 'ʃ_ɑː', 'u_ə', 'ə_eː'}
/s̪/:  {'ɪ_iː', '#_ɪ', '#_ɑː', '#_iː', 'ɑː_ə', 'k_ɑː', 'ɪ_ɑː', 'ɪ_eː', '#_oː', '#_eː', 'ɑː_t̪', 'ə_ə', '#_ə', 'ə_uː', '#_u', 'uː_ɑː', 'ɪ_ə', 'ə_ə̃', 'ɑː_ɪ', 'u_ə', 'ɑː_ɑː', '#_ʈ', 'u_eː', 'ə_eː'}
/n̪/:  {'u_oː', '#_ɪ', 'eː_ɑː', 'oː_õː', '#_ɑː', 'ɑː_iː', '#_iː', 'ɑː_ə', 'u_ɦ', 'u_ɪ', 'ɾ_eː', 'eː_ɪ', 'ɪ_eː', 'ɪ_ɑː', '#_eː', 'ɑː_d͡', 'iː_ə', 'ə_ɑː', 'ə_ə', '#_ə', 'oː_eː', 'ɪ̃_eː', 'ə_iː', 'iː_eː', '#_u', 'ɪ_ə', 'uː_eː', 'u_ə', 'ɑː_ɑː', 'ə_eː'}
/ĩː/:  {'ɦ_#'}
/bʰ/:  {'#_ə', '#_ɑː', 'ə_iː', '#_eː', '#_uː', '#_iː'}

--------- POSSIBLE ALLOPHONES -----------
/õː/:  {'l_#', 'ʃ_#', 'ɾ_#', 'j_#', 'n̪_#', 'd̪_#'}
/ɛ/:  {'ɦ_#', 'p_ɦ', 'b_ʈʰ'}
/g/:  {'#_ə', 'eː_iː', 'eː_ɑː', 'oː_ɪ', 'ə̃_oː', 'oː_ə', 'ɑː_eː', 'ɑː_ə', 'oː_iː', 'ẽː_eː', 'ə_ɑː', 'ə_ə', '#_u', 'ũː_ɑː'}
/d̪ʰ/:  {'#_ə', '#_oː', 'ə̃_ɑː', 'ə̃_eː', 'ɑː_ɪ', '-_oː', '#_ə̃', '#_iː', 'u_ə', 'ɪ_ə'}
/ə̃/:  {'l_g', 'b_d̪', 's̪_d̪', 'm_z', 'd̪ʰ_d̪ʰ'}
/ʃ/:  {'t͡_ə', 't͡_ɑː', '#_u', 'eː_ə', '#_ɑː', 'ɪ_t̪', 't͡_iː', '#_eː', 't͡_t͡', 't͡_ɪ', 't͡_oː', 't͡_õː', 't͡_u'}
/ɔː/:  {'kʰ_ɾ'}
/ɛː/:  {'ʋ_s'}
/s/:  {'ɛː_eː'}

```

The map is written to `files/env.dat`.

### 4. `find_allophones.py`

This script lists possible allophones of the previously identified phonemes by seeing which sounds are in complementary distribution to each phoneme.

The `env` mapping is sourced from `files/env.dat` and the list of phonemes from `files/phonemes.dat`. 
Together, these are used to create a mapping from `phoneme -> set of allophones`.

The mapping is written to `files/allophones.dat`. 

The phonemes along with their respective possible allophones are printed to `stdout`.
Example:

```
Phoneme         Possible Allophones

l       {'ũː', 't͡', 'ɔː', 's', 'ʒ', 'ũ', 'ɔ', '-', 'õː', 'ʒʰ', 'ɛ', 'ẽː', 'ə̃', 'ɪ̃', 'ʃʰ', 'ɖʰ', 'd͡', 'ɛː'}
ʋ       {'s', 'z', 'ə̃', 'ɖ', 't͡', 'ɔː', 'ũ', 'õː', 'ʒʰ', 'ɛ', 'ẽː', 'ɳ', 'ɔ', 'ʃʰ', 'ɖʰ', 'ũː', 'ʒ', 'ɪ̃', 'd͡', 'ɛː'}
k       {'ũː', 't͡', 'ɔː', 's', 'ʒ', 'ɔ', 'õː', 'ʒʰ', 'ɛ', 'ẽː', 'ə̃', 'ʃʰ', 'ɖʰ', 'd͡', 'ɛː'}
ɦ       {'ũː', 't͡', 'ɔː', 's', 'ʒ', 'ũ', 'ɔ', 'õː', 'ʒʰ', 'ɛ', 'ẽː', 'ə̃', 'ɪ̃', 'ʃʰ', 'ɖʰ', 'd͡', 'ɛː'}
...
```

## Notes

- Combined sounds like t͡ʃ are treated as two seperate sounds, namely t͡ and ʃ.


## License & Contributions

All contributions are welcome. This code is licensed under the [BSD-3-Clause License](https://github.com/clocked07/phonolyzer/blob/trunk/LICENSE).
