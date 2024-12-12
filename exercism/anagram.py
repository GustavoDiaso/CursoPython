from win32file import TF_REUSE_SOCKET


def return_anagram(target: str, *candidates) -> list:
    target = target.strip().lower()
    anagrams = []

    def is_anagram(word1:str, word2:str) -> bool:
        if len(word1) == len(word2):
            answer = True
            for letter in word1:
                if letter not in word2:
                    answer = False

            return  answer

        return  False


    for word in candidates:
        if is_anagram(target, word.lower()):
            anagrams.append(word)


    return anagrams

print(return_anagram('stone', "tones", "banana", "tons", "notes", "Seton"))