from collections import Counter

class Level21Solver(object):

    def __init__(self, dict_file):
       
        self.dict_words = []
        dict_file = open(dict_file, "r+")
        for word in dict_file:
            self.dict_words.append(word.strip('\n'))

    def get_correct_word(self, scrambled_word):
        
        for word in self.dict_words:
            
            if len(word) == len(scrambled_word):
                word_dict = sorted(Counter(word).items())
                scrambled_dict = sorted(Counter(scrambled_word).items())
                if word_dict == scrambled_dict:
                    return word

    def unscramble_text(self, scrambled_text):
        
        solution = []
        scrambled_words = scrambled_text.split(';')
        
        for scrambled_word in scrambled_words:
            correct_word = self.get_correct_word(scrambled_word)
            solution.append(correct_word)
        
        return ';'.join(solution)

def main():
   
    solver = Level21Solver("dictionary.txt")
    scrambled_text = raw_input("Enter the text to unscramble:\n")
    solution = solver.unscramble_text(scrambled_text)
    print solution

if __name__ == "__main__":
    main()