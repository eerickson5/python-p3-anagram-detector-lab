# your code goes here!
import ipdb
class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, words):
        self_array = sorted(list(self.word))
        matches = []
        words_as_arrays = [sorted(list(word)) for word in words]
        for i in range(len(words_as_arrays)):
            if words_as_arrays[i] == self_array:
                matches.append(words[i])
        return matches
