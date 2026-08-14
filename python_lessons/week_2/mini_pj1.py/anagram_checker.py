class AnagramCheker:
    def __init__(self):
        self.words_from_list = self.read_file()
        

    def read_file(self):
        with open ('sowpods.txt', 'r') as file:
            return file.read().splitlines()
        
    def is_valid_word(self, word):
        if word.upper() in self.words_from_list:
            return True
        else:
            return False

    def is_anagram(self, word1, word2):
        if sorted(word1) == sorted(word2):
            return True
        else:
            return False

    def get_anagrams(self, word):
        anagrams = []
        for i in self.words_from_list:
            if self.is_anagram(word.upper(), i):
                if word.upper() != i:
                    anagrams.append(i)
        return anagrams

user_input = str(input('Input word for check: '))
anagram_checker = AnagramCheker()
if anagram_checker.is_valid_word(user_input):
    anagrams = anagram_checker.get_anagrams(user_input)
    print(f'Found anagrams: {anagrams}')
else:
    print(f'The word {user_input} is not valid')





